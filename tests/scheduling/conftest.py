import pytest
from tests.utils.db_utils import teardown_db, setup_db
from tests.utils.scheduling_faker import get_physical_address, get_web_address, get_web_addresses, get_lecture_schedule, get_appointment, get_appointments
from tests.utils.program_faker import get_lecture
from ayat import db
from tests.users.conftest import blank


@pytest.fixture
def web_address():
    setup_db()
    web_address = get_web_address()
    db.session.add(web_address)
    db.session.commit()
    yield web_address
    teardown_db()


@pytest.fixture
def physical_address():
    setup_db()
    physical_address = get_physical_address()
    db.session.add(physical_address)
    db.session.commit()
    yield physical_address
    teardown_db()


@pytest.fixture
def schedule():
    setup_db()
    schedule = get_lecture_schedule()
    db.session.add(schedule)
    db.session.commit()
    yield schedule
    teardown_db()


@pytest.fixture
def appointment():
    setup_db()
    appointment = get_appointment()
    db.session.add(appointment)
    db.session.commit()
    yield appointment
    teardown_db()


@pytest.fixture
def appointments():
    setup_db()
    appointments = get_appointments()
    for appointment in appointments:
        db.session.add(appointment)
    db.session.commit()
    yield appointments
    teardown_db()


@pytest.fixture
def inconsistent_web_addresses():
    setup_db()
    web_addresses = get_web_addresses()
    web_addresses[1].url = web_addresses[0].url
    for web_address in web_addresses:
        db.session.add(web_address)
    db.session.commit()
    yield web_addresses
    teardown_db()


@pytest.fixture
def inconsistent_appointments():
    """ uniqueness among 'day', 'start_hour', 'end_hour', 'event_address_id' is violated """
    setup_db()
    appointments = get_appointments()
    appointments[1].day = appointments[0].day
    appointments[1].start_hour = appointments[0].start_hour
    appointments[1].end_hour = appointments[0].end_hour
    for appointment in appointments:
        db.session.add(appointment)
    db.session.commit()
    yield appointments
    teardown_db()