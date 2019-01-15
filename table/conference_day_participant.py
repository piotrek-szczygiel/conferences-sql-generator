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

    def __post_init__(self):
        ConferenceDayParticipant.ID += 1

        self._attending_workshop = False

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

            choose = random.sample(db.participant, p_count + s_count)
            participants = choose[:p_count]
            students = choose[p_count:]

            conf_day = db.conference_day[booking.conference_day_id]
            conf_date = conf_day.start_date
            conf_day = (conf_date.year, conf_date.month, conf_date.day)

            for participant in participants:
                if conf_day in participant._conferences:
                    continue

                participant._conferences.append(conf_day)
                result.append(ConferenceDayParticipant(
                    ConferenceDayParticipant.ID,
                    participant.id,
                    booking.id,
                    None))

            for student in students:
                if conf_day in student._conferences:
                    continue

                student._conferences.append(conf_day)
                result.append(ConferenceDayParticipant(
                    ConferenceDayParticipant.ID,
                    student.id,
                    booking.id,
                    str(random.randint(210000, 299999))))

        return result
