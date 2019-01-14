import random
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
    def __post_init__():
        Participant.ID += 1

    @staticmethod
    def random(db):
        result = []
        for _ in range(random.randint(len(db.client) * 5,
                                      len(db.client) * 15)):
            result.append(Participant(
                Participant.ID,
                fake.first_name(),
                fake.last_name(),
                fake.email()))

        return result
