from dataclasses import dataclass

from fake import fake


@dataclass
class Participant:
    TABLE = 'participant'
    ID = 1

    id: int
    first_name: str
    last_name: str
    email: str

    @staticmethod
    def __post_init__():
        Participant.ID += 1

    @staticmethod
    def random():
        return Participant(
            Participant.ID,
            fake.first_name(),
            fake.last_name(),
            fake.email()
        )

    @staticmethod
    def randoms(count):
        return [Participant.random() for _ in range(count)]
