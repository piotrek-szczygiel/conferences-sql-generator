import random
from dataclasses import dataclass

from fake import fake


@dataclass
class Conference:
    TABLE = 'conference'
    ID = 1

    id: int
    name: str
    price_max: int
    student_price_percent: float

    @staticmethod
    def __post_init__():
        Conference.ID += 1

    @staticmethod
    def random():
        return Conference(
            Conference.ID,
            'Konferencja ' + fake.catch_phrase(),
            random.randint(10, 101),
            1.0 if random.randint(0, 10) > 7 else round(random.uniform(0.2, 0.9), 2)
        )
