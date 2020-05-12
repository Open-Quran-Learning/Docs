from ayat.models.scheduling import Appointment, WebAddress, PhysicalAddress, Schedule
from ayat import db
from tests.utils.db_utils import check_data_inconsistency


def test_web_address_blank(blank):
    assert [] == WebAddress.query.all()


def test_physical_address_blank(blank):
    assert [] == PhysicalAddress.query.all()


def test_appointment_blank(blank):
    assert [] == Appointment.query.all()


def test_schedule_blank(blank):
    assert [] == Schedule.query.all()


def test_web_address_has_addresses(web_address):
    result = WebAddress.query.first()
    assert web_address.equals(result)


def test_physical_address_has_address(physical_address):
    result = PhysicalAddress.query.first()
    assert physical_address.equals(result)


def test_schedule_has_schedule(schedule):
    result = Schedule.query.first()
    assert schedule.equals(result)


def test_appointment_has_appointment(appointment):
    result = Appointment.query.first()
    assert appointment.equals(result)


def test_schedule_uniqueness_inconsistency(inconsistent_web_addresses):
    check_data_inconsistency(inconsistent_web_addresses)

def test_appointment_uniqueness_inconsistency(inconsistent_appointments):
    check_data_inconsistency(inconsistent_appointments)


def test_get_appointments_with_the_same_address(web_address, appointments):
    result = False
    web_address.appointment=[]
    for appointment in appointments:
        web_address.appointment.append(appointment)
    db.session.commit()
    result_web_address = WebAddress.query.first()
    result_appointments = result_web_address.appointment
    for result_appointment in result_appointments:
        for expected_appointment in web_address.appointment:
            if result_appointment.equals(expected_appointment):
                result = True
    assert result

