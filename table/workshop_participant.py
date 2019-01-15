import random
from dataclasses import dataclass


@dataclass
class WorkshopParticipant:
    TABLE = 'workshop_participant'
    ID = 0

    id: int
    conference_day_participant_id: int
    workshop_booking_id: int

    @staticmethod
    def __post_init__():
        WorkshopParticipant.ID += 1

    @staticmethod
    def random(db):
        result = []
        for work_booking in db.workshop_booking:
            if random.randint(0, 10) > 8:
                continue

            conf_participants = []
            for conf_participant in db.conference_day_participant:
                if (conf_participant._attending_workshop or
                        conf_participant.conference_day_booking_id
                        != work_booking.conference_day_booking_id):
                    continue

                conf_participants.append(conf_participant)

            count = min(work_booking.participants_count, len(conf_participants))
            work_participants = random.sample(conf_participants, count)

            for participant in work_participants:
                # TODO: let participant attend multiple workshops a day if they don't overlap
                participant._attending_workshop = True
                result.append(WorkshopParticipant(
                    WorkshopParticipant.ID,
                    participant.id,
                    work_booking.id))

        return result
