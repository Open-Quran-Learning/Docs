import pytest
from ayat.models.users import User, Student, Staff, Guardian
import datetime
from tests.utils.db_utils import clean_user


@pytest.fixture
def test_student():
    birth_date = datetime.datetime(day=17, month=10, year=1996)
    registeration_date = datetime.datetime(day=30, month=4, year=2020)
    student = Student(name='Mohamed', email='moh@yahoo.com', birth_date=birth_date, country_name='Egypt',
                           phone_number='01256468680', gender=True,
                           password='moh123', is_activated=True, registeration_date=registeration_date, type='student')
    yield student
    clean_user()


@pytest.fixture
def test_staff():
    birth_date = datetime.datetime(day=17, month=10, year=1996)
    registeration_date = datetime.datetime(day=30, month=4, year=2020)
    staff = Staff(name='Hazem', email='staff1@yahoo.com', birth_date=birth_date, registeration_date=registeration_date,
                       country_name='Egypt', phone_number='0111242',
                       gender=True, password='staff111', is_activated=True, type='staff')
    yield staff
    clean_user()

guardian = Guardian(email='guardian1@yahoo.com', phone_number='01010')

