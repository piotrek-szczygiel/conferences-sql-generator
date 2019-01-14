import datetime
import random
from dataclasses import dataclass

from fake import fake


@dataclass
class Payment:
    TABLE = 'payment'
    ID = 0

    id: int
    value: float
    date: datetime
    type: str
    is_cancelled: bool
    conference_booking_id: int

    @staticmethod
    def __post_init__():
        Payment.ID += 1

    @staticmethod
    def random(db):
        result = []
        for conf_booking in db.conference_booking:
            for _ in range(random.randint(0, 2)):
                result.append(Payment(
                    Payment.ID,
                    round(random.uniform(10.0, 100.0), 2),
                    fake.past_datetime(start_date=conf_booking.booking_date),
                    random.choice(['przelew bankowy',
                                   'karta płatnicza',
                                   'BLIK',
                                   'PayPal']),
                    True if random.randint(0, 10) > 8 else False,
                    conf_booking.id))

        return result
