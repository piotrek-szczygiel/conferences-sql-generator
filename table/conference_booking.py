import datetime
import random
from dataclasses import dataclass

from fake import fake


@dataclass
class ConferenceBooking:
    TABLE = 'conference_booking'
    ID = 1

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
    def randoms(conferences, clients):
        conferences_bookings = []
        for client in random.choices(clients, k=int(len(clients) * 0.9)):
            for conference in random.choices(conferences, k=random.randint(1, 4)):
                conferences_bookings.append(ConferenceBooking.random(conference, client))

        return conferences_bookings
