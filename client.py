from dataclasses import dataclass
from typing import Optional

from fake import fake


@dataclass
class Client:
    TABLE = 'client'

    is_company: bool
    name: str
    email: str
    password: str
    nip: Optional[int]
    address: Optional[str]

    @staticmethod
    def random_company():
        return Client(
            True,
            fake.company(),
            fake.email(),
            fake.sha256(),
            fake.random_number(digits=10),
            fake.address().replace('\n', ', ')
        )

    @staticmethod
    def random_individual():
        return Client(
            False,
            fake.first_name() + ' ' + fake.last_name(),
            fake.email(),
            fake.sha256(),
            None,
            fake.address().replace('\n', ', ') if fake.boolean() else ''
        )
