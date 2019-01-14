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
    def randoms(db):
        conference_prices = []
        for conference in db.conference:
            days = random.randint(5, 15)
            increment = (0.5 / days) * random.uniform(0.6, 0.9)
            for days_before in range(1, days):
                conference_prices.append(ConferencePrice(
                    ConferencePrice.ID,
                    conference.id,
                    round(1.0 - days_before * increment, 2),
                    days_before
                ))

        return conference_prices
