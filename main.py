import sys

import sql
from client import Client
from conference import Conference
from participant import Participant

if __name__ == '__main__':
    clients = [Client.random() for _ in range(3)]
    participants = [Participant.random() for _ in range(5)]
    conferences = [Conference.random() for _ in range(2)]

    result = '\n'.join([sql.put(conferences),
                        sql.put(clients),
                        sql.put(participants)])

    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
