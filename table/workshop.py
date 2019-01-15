import datetime
import random
from dataclasses import dataclass

from fake import fake


@dataclass
class Workshop:
    TABLE = 'workshop'
    ID = 0

    id: int
    conference_day_id: int
    name: str
    start_date: datetime
    end_date: datetime
    price: float
    participants_limit: int
    location: str

    def __post_init__(self):
        Workshop.ID += 1

        self._participants = 0

    @staticmethod
    def random(db):
        result = []
        for conf_day in db.conference_day:
            for _ in range(random.randint(0, 3)):
                start_min = conf_day.start_date
                start_max = (
                        conf_day.end_date
                        - datetime.timedelta(hours=random.randint(1, 4)))

                start = fake.date_time_between(start_date=start_min,
                                               end_date=start_max)

                start = start.replace(second=0, minute=start.minute // 10 * 10)

                end_min = start + datetime.timedelta(hours=1)
                end_max = conf_day.end_date

                end = fake.date_time_between(start_date=end_min,
                                             end_date=end_max)

                end = end.replace(second=0, minute=end.minute // 10 * 10)

                price = 0.0
                if random.randint(0, 10) > 6:
                    price = round(random.uniform(10.0, 100.0), 2)

                result.append(Workshop(
                    Workshop.ID,
                    conf_day.id,
                    fake.catch_phrase(),
                    start,
                    end,
                    price,
                    random.randint(30, conf_day.participants_limit),
                    fake.address()))

        return result
