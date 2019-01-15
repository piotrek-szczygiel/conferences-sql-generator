import random
from dataclasses import dataclass

from fake import fake


@dataclass
class WorkshopBooking:
    TABLE = 'workshop_booking'
    ID = 0

    id: int
    workshop_id: int
    conference_day_booking_id: int
    participants_count: int

    def __post_init__(self):
        WorkshopBooking.ID += 1

        self._participants = 0

    @staticmethod
    def random(db):
        result = []
        for booking in db.conference_day_booking:
            for work in db.workshop:
                if work._participants >= work.participants_limit:
                    continue

                if work.conference_day_id != booking.conference_day_id:
                    continue

                if fake.boolean():
                    continue

                count = random.randint(1, booking.participants_count
                                       + booking.students_count)

                if count + work._participants > work.participants_limit:
                    if fake.boolean():
                        continue
                    else:
                        count = work.participants_limit - work._participants

                work._participants += count

                result.append(WorkshopBooking(
                    WorkshopBooking.ID,
                    work.id,
                    booking.id,
                    count
                ))

        return result
