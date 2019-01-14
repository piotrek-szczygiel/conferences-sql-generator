import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class ConferenceDayParticipant:
    TABLE = 'conference_day_participant'
    ID = 0

    id: int
    participant_id: int
    conference_day_booking_id: int
    student_id: Optional[str]

    @staticmethod
    def __post_init__():
        ConferenceDayParticipant.ID += 1

    @staticmethod
    def random(db):
        result = []
        for booking in db.conference_day_booking:
            if random.randint(0, 10) > 8:
                continue

            p_count = random.randint(int(booking.participants_count // 2),
                                     booking.participants_count)

            s_count = random.randint(int(booking.students_count // 2),
                                     booking.students_count)

            participants = random.choices(db.participant, k=p_count)
            students = random.choices(db.participant, k=s_count)

            for participant in participants:
                result.append(ConferenceDayParticipant(
                    ConferenceDayParticipant.ID,
                    participant.id,
                    booking.id,
                    None))

            for student in students:
                result.append(ConferenceDayParticipant(
                    ConferenceDayParticipant.ID,
                    student.id,
                    booking.id,
                    str(random.randint(210000, 299999))))

        return result
