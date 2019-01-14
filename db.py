import sql
from table.client import Client
from table.conference import Conference
from table.conference_booking import ConferenceBooking
from table.conference_day import ConferenceDay
from table.conference_day_booking import ConferenceDayBooking
from table.conference_day_participant import ConferenceDayParticipant
from table.conference_price import ConferencePrice
from table.participant import Participant
from table.payment import Payment
from table.workshop import Workshop


class DB:
    def __init__(self, size):
        self.size = size

        self.conference = []
        self.client = []
        self.participant = []
        self.conference_day = []
        self.conference_price = []
        self.conference_booking = []
        self.payment = []
        self.conference_day_booking = []
        self.conference_day_participant = []
        self.workshop = []

    def generate(self):
        self.conference = Conference.random(self)
        self.client = Client.random(self)
        self.participant = Participant.random(self)
        self.conference_day = ConferenceDay.random(self)
        self.conference_price = ConferencePrice.random(self)
        self.conference_booking = ConferenceBooking.random(self)
        self.payment = Payment.random(self)
        self.conference_day_booking = ConferenceDayBooking.random(self)
        self.conference_day_participant = ConferenceDayParticipant.random(self)
        self.workshop = Workshop.random(self)

    def to_sql(self):
        return (sql.clear_db() +
                sql.put_all([
                    self.conference,
                    self.conference_day,
                    self.client,
                    self.conference_booking,
                    self.conference_day_booking,
                    self.participant,
                    self.conference_day_participant,
                    self.conference_price,
                    self.payment,
                    self.workshop
                ]))
