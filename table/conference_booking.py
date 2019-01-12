import datetime
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
