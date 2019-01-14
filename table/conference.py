import random
from dataclasses import dataclass

from fake import fake


@dataclass
class Conference:
    TABLE = 'conference'
    ID = 0

    id: int
    name: str
    price_max: int
    student_price_percent: float

    @staticmethod
    def __post_init__():
        Conference.ID += 1

    @staticmethod
    def random(db):
        result = []
        for _ in range(db.size):
            if random.randint(0, 10) > 8:
                student_price_percent = 1.0
            else:
                student_price_percent = round(random.uniform(0, 0.7), 2)

            result.append(Conference(
                Conference.ID,
                fake.catch_phrase(),
                random.randint(10, 100),
                student_price_percent))

        return result
