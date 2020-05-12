from ayat import db


class Appointment(db.Model):
    __tablename__ = 'appointment'
    appointment_id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer, nullable=False)
    start_hour = db.Column(db.Time, nullable=False)
    end_hour = db.Column(db.Time, nullable=False)
    event_address_id = db.Column(db.Integer, db.ForeignKey('event_address.event_address_id'), nullable=False)
    schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.schedule_id'), nullable=False)
    db.UniqueConstraint('day', 'start_hour', 'end_hour', 'event_address_id')

    schedule = db.relationship("Schedule")
    event_address = db.relationship("EventAddress")

    def __repr__(self):
        Info_text = f'Day {self.day}\t' \
                    f'Start Hour {self.start_hour}\t' \
                    f'End Hour {self.end_hour}\n'

        return Info_text

    def equals(self, appointment):
        if self.day == appointment.day \
                and self.start_hour == appointment.start_hour \
                and self.end_hour == appointment.end_hour \
                and self.event_address_id == appointment.event_address_id:
            return True
        return False


##############################################################################################

class Schedule(db.Model):
    __tablename__ = 'schedule'
    schedule_id = db.Column(db.Integer, primary_key=True)
    recurrent = db.Column(db.Boolean, nullable=False)
    appointment = db.relationship("Appointment", back_populates="schedule")

    type = db.Column(db.VARCHAR(20), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'schedule',
                       'polymorphic_on': type}

    def __repr__(self):
        Info_text = f'Is recurrent?? {self.recurrent}\t'
        return Info_text

    def equals(self, schedule):
        if self.schedule_id == schedule.schedule_id:
            return True
        return False


class LectureSchedule(Schedule):
    __tablename__ = "lecture_schedule"
    lecture_schedule_id = db.Column(db.Integer, db.ForeignKey('schedule.schedule_id'), primary_key=True)
    lecture_id = db.Column(db.Integer, db.ForeignKey("lecture.lecture_id"), nullable=False)
    lecture = db.relationship("Lecture", backref=db.backref('schedules'))
    __mapper_args__ = {'polymorphic_identity': 'lecture_schedule'}


##############################################################################################

class EventAddress(db.Model):
    __tablename__ = "event_address"
    event_address_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.VARCHAR(30), nullable=False)
    appointment = db.relationship("Appointment", back_populates="event_address")

    type = db.Column(db.VARCHAR(20), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'event_address',
                       'polymorphic_on': type}

    def __repr__(self):
        Info_text = f'{self.__class__.__name__} Id: {self.event_address_id}.'

        return Info_text


##############################################################################################


class PhysicalAddress(EventAddress):
    __tablename__ = "physical_address"
    event_address_id = db.Column(db.Integer, db.ForeignKey("event_address.event_address_id"), primary_key=True)
    country_name = db.Column(db.VARCHAR(30), nullable=False)
    address_details = db.Column(db.VARCHAR(150), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'physical_address'}

    def __repr__(self):
        Info_text = f'{super().__repr__()}\t' \
                    f'Country Name: {self.country_name}\t' \
                    f'Address Details: {self.address_details}\n'

        return Info_text

    def equals(self, physical_address):
        if self.country_name == physical_address.country_name \
                and self.address_details == physical_address.address_details:
            return True
        return False


##################################################################################################


class WebAddress(EventAddress):
    __tablename__ = "web_address"
    event_address_id = db.Column(db.Integer, db.ForeignKey("event_address.event_address_id"), primary_key=True)
    url = db.Column(db.String, nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'web_address'}

    def __repr__(self):
        Info_text = f'{super().__repr__()}\t' \
                    f'URL: {self.url}\n'

        return Info_text

    def equals(self, web_address):
        if self.url == web_address.url:
            return True
        return False
