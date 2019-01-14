import pyodbc
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
    conf_count = 10

    db = DB(conf_count)

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
                  db.conference_day,
                  db.client,
                  db.conference_booking,
                  db.conference_day_booking,
                  db.participant,
                  db.conference_day_participant,
                  db.conference_price,
                  db.payment,
              ]))

    # Write result to file or send directly to SQL server
    if len(sys.argv) >= 2:
        file_name = sys.argv[2]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        with open('conn.txt', 'r') as connection:
            print('connecting to database...')
            conn = pyodbc.connect(connection.read())

            print('inserting data for {} conferences...'.format(conf_count))
            cursor = conn.cursor()
            cursor.execute(result)
            conn.commit()
            conn.close()
            print('data successfully inserted')
