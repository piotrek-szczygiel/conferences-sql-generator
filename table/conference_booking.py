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
    def random(conference, client):
        return ConferenceBooking(
            ConferenceBooking.ID,
            conference.id,
            client.id,
            fake.past_datetime(start_date='-1y')
        )

    @staticmethod
    def randoms(db):
        result = []
        for client in random.choices(db.client,
                                     k=int(len(db.client) // 1.2)):
            for conference in random.choices(db.conference,
                                             k=random.choice([1, 1, 1, 2, 3])):
                result.append(
                    ConferenceBooking.random(conference, client))

        return result
