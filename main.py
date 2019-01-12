import sys

import sql
from client import Client
from fake import fake
from participant import Participant

if __name__ == '__main__':
    clients = []
    for _ in range(10):
        if fake.boolean():
            clients.append(Client.random_company())
        else:
            clients.append(Client.random_individual())

    participants = []
    for _ in range(15):
        participants.append(Participant.random())

    result = (sql.delete_and_insert(clients)
              + sql.delete_and_insert(participants)
              + sql.insert(Client.random_individual()))

    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
