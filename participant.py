from dataclasses import dataclass

from fake import fake


@dataclass
class Participant:
    TABLE = 'participant'

    first_name: str
    last_name: str
    email: str

    @staticmethod
    def random():
        return Participant(
            fake.first_name(),
            fake.last_name(),
            fake.email()
        )
