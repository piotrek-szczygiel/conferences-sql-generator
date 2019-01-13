import random
import sys

import sql
from table.client import Client
from table.conference import Conference
from table.conference_booking import ConferenceBooking
from table.participant import Participant
from table.payment import Payment

if __name__ == '__main__':
    clients = [Client.random() for _ in range(3)]
    participants = [Participant.random() for _ in range(5)]
    conferences = [Conference.random() for _ in range(2)]

    conference_bookings = []
    for client in random.choices(clients, k=int(len(clients) * 0.9)):
        for conference in random.choices(conferences, k=random.randint(1, 4)):
            conference_bookings.append(ConferenceBooking.random(conference, client))

    payments = []
    for conference_booking in conference_bookings:
        for _ in range(random.randint(0, 4)):
            payments.append(Payment.random(conference_booking))

    result = '\n'.join([sql.start(),
                        sql.put(conferences),
                        sql.put(clients),
                        sql.put(participants),
                        sql.put(conference_bookings),
                        sql.put(payments)])

    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
