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
        if random.randint(0, 10) > 7:
            student_price_percent = 1.0
        else:
            student_price_percent = round(random.uniform(0.2, 0.9), 2)

        return Conference(
            Conference.ID,
            fake.catch_phrase(),
            random.randint(10, 101),
            student_price_percent
        )

    @staticmethod
    def randoms(count):
        return [Conference.random() for _ in range(count)]
