from fake import fake
from sql import *


def delete_clients():
    return sql_delete('client')


def insert_clients(count):
    clients = []

    for _ in range(count):
        if fake.boolean():
            clients.append(random_client_individual())
        else:
            clients.append(random_client_company())

    return sql_insert('client',
                      [
                          'is_company',
                          'name',
                          'email',
                          'password',
                          'nip',
                          'address'
                      ],
                      clients
                      )


def random_client_company():
    return [
        1,
        fake.company(),
        fake.email(),
        fake.sha256(),
        fake.random_number(digits=10),
        fake.address().replace('\n', ', ')
    ]


def random_client_individual():
    return [
        0,
        fake.first_name() + ' ' + fake.last_name(),
        fake.email(),
        fake.sha256(),
        '',
        fake.address().replace('\n', ', ') if fake.boolean() else ''
    ]
