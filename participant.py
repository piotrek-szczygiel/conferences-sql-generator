from dataclasses import dataclass

from fake import fake


@dataclass
class Participant:
    TABLE = 'participant'
    ID = 0

    id: int
    first_name: str
    last_name: str
    email: str

    @staticmethod
    def random():
        Participant.ID += 1

        return Participant(
            Participant.ID,
            fake.first_name(),
            fake.last_name(),
            fake.email()
        )
