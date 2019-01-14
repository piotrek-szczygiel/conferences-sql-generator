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
    def randoms(db):
        result = []
        for conference_day_booking in db.conference_day_booking:
            joined = random.choices(
                db.participant,
                k=conference_day_booking.participants_count +
                  conference_day_booking.students_count)
            participants = joined[:conference_day_booking.participants_count]
            students = joined[conference_day_booking.participants_count:]

            for participant in participants:
                result.append(ConferenceDayParticipant(
                    ConferenceDayParticipant.ID,
                    participant.id,
                    conference_day_booking.id,
                    None
                ))

            for student in students:
                result.append(ConferenceDayParticipant(
                    ConferenceDayParticipant.ID,
                    student.id,
                    conference_day_booking.id,
                    str(random.randint(200000, 300000))
                ))

        return result