import random
from dataclasses import dataclass


@dataclass
class ConferencePrice:
    TABLE = 'conference_price'
    ID = 0

    id: int
    conference_id: int
    price_percent: float
    days_before: int

    @staticmethod
    def __post_init__():
        ConferencePrice.ID += 1

    @staticmethod
    def random(db):
        result = []
        for conf in db.conference:
            days = random.randint(5, 15)
            increment = (0.5 / days) * random.uniform(0.6, 0.9)

            for days_before in range(1, days):
                result.append(ConferencePrice(
                    ConferencePrice.ID,
                    conf.id,
                    round(1.0 - days_before * increment, 2),
                    days_before))

        return result
