import datetime
import random
from dataclasses import dataclass

from fake import fake


@dataclass
class ConferenceBooking:
    TABLE = 'conference_booking'
    ID = 0

    id: int
    conference_id: int
    client_id: int
    booking_date: datetime

    @staticmethod
    def __post_init__():
        ConferenceBooking.ID += 1

    @staticmethod
    def randoms(db):
        result = []
        for cl in random.choices(db.client, k=int(len(db.client) // 1.2)):
            for conf in random.choices(db.conference, k=random.randint(0, 4)):

                date = None
                for cd in db.conference_day:
                    if cd.conference_id == conf.id:
                        date = cd.start_date
                        break

                if date is None:
                    continue

                if date > datetime.datetime.now():
                    date = datetime.datetime.now()

                date_before = date - datetime.timedelta(weeks=20)

                result.append(ConferenceBooking(
                    ConferenceBooking.ID,
                    conf.id,
                    cl.id,
                    fake.date_time_between(
                        start_date=date_before,
                        end_date=date)))

        return result
