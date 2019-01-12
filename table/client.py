from dataclasses import dataclass
from typing import Optional

from fake import fake


@dataclass
class Client:
    TABLE = 'client'
    ID = 1

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
    def random():
        if fake.boolean():
            return Client.random_individual()
        else:
            return Client.random_company()

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
