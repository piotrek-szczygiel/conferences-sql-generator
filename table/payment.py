import datetime
import random
from dataclasses import dataclass

from fake import fake


@dataclass
class Payment:
    TABLE = 'payment'
    ID = 1

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
    def random(conference_booking):
        return Payment(
            Payment.ID,
            round(random.uniform(10.0, 100.0), 2),
            fake.past_datetime(start_date=conference_booking.booking_date),
            random.choice(['przelew bankowy', 'karta płatnicza', 'BLIK', 'PayPal']),
            True if random.randint(0, 10) == 9 else False,
            conference_booking.id
        )

    @staticmethod
    def randoms(conferences_bookings):
        payments = []
        for conference_booking in conferences_bookings:
            for _ in range(random.randint(0, 4)):
                payments.append(Payment.random(conference_booking))

        return payments
