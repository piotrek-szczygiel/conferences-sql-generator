import random
from dataclasses import dataclass


@dataclass
class ConferenceDayBooking:
    TABLE = 'conference_day_booking'
    ID = 0

    id: int
    participants_count: int
    students_count: int
    conference_day_id: int
    conference_booking_id: int
    is_cancelled: bool

    @staticmethod
    def __post_init__():
        ConferenceDayBooking.ID += 1

    @staticmethod
    def randoms(db):
        result = []
        for conference_booking in db.conference_booking:
            for conference_day in db.conference_day:
                if (conference_booking.conference_id
                        != conference_day.conference_id):
                    continue

                result.append(ConferenceDayBooking(
                    ConferenceDayBooking.ID,
                    random.randint(1, 10),
                    random.randint(0, 2),
                    conference_day.id,
                    conference_booking.id,
                    True if random.randint(0, 10) == 9 else False
                ))

        return result
