import sys

import sql
from table.client import Client
from table.conference import Conference
from table.conference_booking import ConferenceBooking
from table.conference_price import ConferencePrice
from table.participant import Participant
from table.payment import Payment

if __name__ == '__main__':
    participants_count = 10 if len(sys.argv) < 2 else int(sys.argv[1])

    # Generate independent tables (without foreign keys)
    participants = [Participant.random() for _ in range(participants_count)]
    clients = [Client.random() for _ in range(1 + int(participants_count / 2))]
    conferences = [Conference.random() for _ in range(1 + int(participants_count / 10))]

    # Generate dependent tables
    conference_prices = ConferencePrice.randoms(conferences)
    conference_bookings = ConferenceBooking.randoms(conferences, clients)
    payments = Payment.randoms(conference_bookings)

    result = (sql.start() +
              sql.put_all([
                  participants,
                  clients,
                  conferences,
                  conference_prices,
                  conference_bookings,
                  payments]))

    if len(sys.argv) >= 3:
        file_name = sys.argv[2]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
