import sys

import sql
from table.client import Client
from table.conference import Conference
from table.conference_booking import ConferenceBooking
from table.conference_day import ConferenceDay
from table.conference_price import ConferencePrice
from table.participant import Participant
from table.payment import Payment

if __name__ == '__main__':
    size = 10 if len(sys.argv) < 2 else int(sys.argv[1])

    participants = Participant.randoms(size)
    clients = Client.randoms(1 + len(participants) // 2)
    conferences = Conference.randoms(1 + len(clients) // 5)
    conferences_days = ConferenceDay.randoms(conferences)
    conference_prices = ConferencePrice.randoms(conferences)
    conference_bookings = ConferenceBooking.randoms(conferences, clients)
    payments = Payment.randoms(conference_bookings)

    result = (sql.start() +
              sql.put_all([
                  participants,
                  clients,
                  conferences,
                  conferences_days,
                  conference_prices,
                  conference_bookings,
                  payments]))

    if len(sys.argv) >= 3:
        file_name = sys.argv[2]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
