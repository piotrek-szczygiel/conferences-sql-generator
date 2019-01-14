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
            for cd in db.conference_day:
                if cd.conference_id != conference_booking.conference_id:
                    continue

                p_count = random.randint(1, 10)
                s_count = random.randint(0, 2)

                if p_count + s_count + cd._participants > cd.participants_limit:
                    continue

                cd._participants += (p_count + s_count)

                result.append(ConferenceDayBooking(
                    ConferenceDayBooking.ID,
                    p_count,
                    s_count,
                    cd.id,
                    conference_booking.id,
                    True if random.randint(0, 10) == 9 else False
                ))

        return result
