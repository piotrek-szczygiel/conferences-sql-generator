import sys

import sql
from db import DB
from table.client import Client
from table.conference import Conference
from table.conference_booking import ConferenceBooking
from table.conference_day import ConferenceDay
from table.conference_day_booking import ConferenceDayBooking
from table.conference_day_participant import ConferenceDayParticipant
from table.conference_price import ConferencePrice
from table.participant import Participant
from table.payment import Payment

if __name__ == '__main__':
    size = 1 if len(sys.argv) < 2 else int(sys.argv[1])

    db = DB(size)

    db.conference = Conference.randoms(db)
    db.client = Client.randoms(db)
    db.participant = Participant.randoms(db)
    db.conference_day = ConferenceDay.randoms(db)
    db.conference_price = ConferencePrice.randoms(db)
    db.conference_booking = ConferenceBooking.randoms(db)
    db.payment = Payment.randoms(db)
    db.conference_day_booking = ConferenceDayBooking.randoms(db)
    db.conference_day_participant = ConferenceDayParticipant.randoms(db)

    result = (sql.start() +
              sql.put_all([
                  db.conference,
                  db.client,
                  db.participant,
                  db.conference_day,
                  db.conference_price,
                  db.conference_booking,
                  db.payment,
                  db.conference_day_booking,
                  db.conference_day_participant
              ]))

    if len(sys.argv) >= 3:
        file_name = sys.argv[2]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
