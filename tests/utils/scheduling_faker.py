from ayat.models.scheduling import Appointment, EventAddress, WebAddress, PhysicalAddress, Schedule, LectureSchedule
from tests.utils.program_faker import get_lecture
import datetime


def get_lecture_schedule():
    lecture = get_lecture()
    lecture_schedule = LectureSchedule(recurrent=True)
    lecture.schedules.append(lecture_schedule)
    return lecture_schedule


def get_web_address():
    web_address = WebAddress(url="https://www.example.com")
    return web_address


def get_web_addresses():
    web_addresses = [WebAddress(url="https://www.example.com"),
                     WebAddress(url="https://www.khaled.example.com")]
    return web_addresses


def get_physical_address():
    physical_address = PhysicalAddress(country_name="Egypt", address_details="Sharkia-Hehia")
    return physical_address


def get_appointment():
    lecture_schedule = get_lecture_schedule()
    web_address = get_web_address()
    appointment = Appointment(day=3, start_hour=datetime.time(3, 30), end_hour=datetime.time(5, 30),
                              schedule=lecture_schedule, event_address=web_address)
    return appointment


def get_appointments():
    lecture_schedule = get_lecture_schedule()
    web_address = get_web_address()
    appointments = [Appointment(day=3,
                                start_hour=datetime.time(3, 30),
                                end_hour=datetime.time(5, 30),
                                schedule=lecture_schedule,
                                event_address=web_address),
                    Appointment(day=4,
                                start_hour=datetime.time(5, 30),
                                end_hour=datetime.time(7, 30),
                                schedule=lecture_schedule,
                                event_address=web_address)
                    ]
    return appointments
