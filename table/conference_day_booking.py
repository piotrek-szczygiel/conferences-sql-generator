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
    def random(db):
        result = []
        for booking in db.conference_booking:
            for cd in db.conference_day:
                if cd.conference_id != booking.conference_id:
                    continue

                p_count = random.randint(1, 10)
                s_count = random.randint(0, 2)
                count = p_count + s_count

                if count + cd._participants > cd.participants_limit:
                    continue

                cd._participants += count

                result.append(ConferenceDayBooking(
                    ConferenceDayBooking.ID,
                    p_count,
                    s_count,
                    cd.id,
                    booking.id,
                    True if random.randint(0, 10) == 9 else False))

        return result
