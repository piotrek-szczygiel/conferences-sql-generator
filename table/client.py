import random
from dataclasses import dataclass
from typing import Optional

from fake import fake


@dataclass
class Client:
    TABLE = 'client'
    ID = 0

    id: int
    is_company: bool
    name: str
    email: str
    password: str
    nip: Optional[str]
    address: Optional[str]

    @staticmethod
    def __post_init__():
        Client.ID += 1

    @staticmethod
    def random(db):
        result = []
        for _ in range(random.randint(len(db.conference) * 15,
                                      len(db.conference) * 20)):
            if random.randint(0, 10) > 4:
                result.append(Client.random_individual())
            else:
                result.append(Client.random_company())

        return result

    @staticmethod
    def random_company():
        return Client(
            Client.ID,
            True,
            fake.company(),
            fake.email(),
            fake.sha256(),
            str(fake.random_number(digits=10)),
            fake.address().replace('\n', ', ')
        )

    @staticmethod
    def random_individual():
        return Client(
            Client.ID,
            False,
            fake.first_name() + ' ' + fake.last_name(),
            fake.email(),
            fake.sha256(),
            None,
            fake.address().replace('\n', ', ') if fake.boolean() else ''
        )
