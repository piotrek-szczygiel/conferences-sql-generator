import datetime
import random
from dataclasses import dataclass

from fake import fake


@dataclass
class ConferenceDay:
    TABLE = 'conference_day'
    ID = 1

    id: int
    conference_id: int
    participants_limit: int
    start_date: datetime
    end_date: datetime
    location: str

    @staticmethod
    def __post_init__():
        ConferenceDay.ID += 1

    @staticmethod
    def randoms(conferences):
        conferences_days = []
        for conference in conferences:
            start_date = fake.date_time_between(start_date='-3y',
                                                end_date='+1y')

            start_date = start_date.replace(hour=random.randint(8, 11),
                                            minute=0,
                                            second=0)

            days = random.randint(1, 4)
            for i in range(days):
                date = start_date + datetime.timedelta(days=i)

                conferences_days.append(ConferenceDay(
                    ConferenceDay.ID,
                    conference.id,
                    random.randint(150, 250),
                    date,
                    date + datetime.timedelta(hours=random.randint(6, 11)),
                    fake.address().replace('\n', ', ')
                ))

        return conferences_days
