from config import db

# ALL OF THESE CAN BE DELETED OR CHANGED IF WE HAVE TO.
# we can add or delete tables as we need to.
class Test(db.Model):
    __tablename__ = 'test'
    # these are the attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    s_email = db.Column(db.String(100))
    s_name = db.Column(db.String(100))
    s_lang = db.Column(db.String(40))

    # this the default constructor of the class
    def __init__(self,s_email, s_name, s_lang):
        self.s_email = s_email
        self.s_name = s_name
        self.s_lang = s_lang

# I made this second class to test how to add things to a second table in the db.
# this is a super early version of an event date system.
# what we could do is make it compare the numbers in the db to a number on the interactive calendar.
class Event(db.Model):
    __tablename__ = 'testEvent'
    id = db.Column(db.Integer, primary_key=True)
    e_month = db.Column(db.Integer)
    e_day = db.Column(db.Integer)
    e_year = db.Column(db.Integer)

    def __init__(self, e_month, e_day, e_year):
        self.e_month = e_month
        self.e_day = e_day
        self.e_year = e_year

# this is a much better version of what i expect we'll need to store for events, excluding language and assessment type
class fullEvent(db.Model):
    __tablename__ = 'newEvent'
    id = db.Column(db.Integer, primary_key=True)
    student_email = db.Column(db.String(100))
    event_date = db.Column(db.String(40))
    event_room = db.Column(db.String(40))

    def __init__(self, student_email, event_date, event_room):
        self.student_email = student_email
        self.event_date = event_date
        self.event_room = event_room

