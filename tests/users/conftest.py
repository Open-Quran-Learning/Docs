import pytest
from tests.utils.db_utils import teardown_db, setup_db
from tests.utils.user_faker import get_student, get_students, get_staff_member, get_staff, get_guardians, \
    get_permissions, get_guardian, get_permission
from ayat import db


@pytest.fixture
def blank():
    setup_db()
    yield
    teardown_db()


@pytest.fixture
def student():
    setup_db()
    student = get_student()
    db.session.add(student)
    db.session.commit()
    yield student
    teardown_db()


@pytest.fixture
def students():
    setup_db()
    students = get_students()
    for student in students:
        db.session.add(student)
    db.session.commit()
    yield students
    teardown_db()


@pytest.fixture
def staff_member():
    setup_db()
    staff_member = get_staff_member()
    db.session.add(staff_member)
    db.session.commit()
    yield staff_member
    teardown_db()


@pytest.fixture
def staff():
    setup_db()
    staff = get_staff()
    for staff_member in staff:
        db.session.add(staff_member)
    db.session.commit()
    yield staff
    teardown_db()


@pytest.fixture
def inconsistent_users():
    setup_db()
    students = get_students()
    students[1].email = students[0].email
    students[2].phone_number = students[0].phone_number
    yield students
    teardown_db()


@pytest.fixture
def guardian():
    setup_db()
    guardian = get_guardian()
    db.session.add(guardian)
    db.session.commit()
    yield guardian
    teardown_db()


@pytest.fixture
def guardians():
    setup_db()
    guardians = get_guardians()
    for guardian in guardians:
        db.session.add(guardian)
    db.session.commit()
    yield guardians
    teardown_db()

@pytest.fixture
def permission():
    setup_db()
    permission = get_permission()
    db.session.add(permission)
    db.session.commit()
    yield permission
    teardown_db()

@pytest.fixture
def permissions():
    setup_db()
    permissions = get_permissions()
    for permission in permissions:
        db.session.add(permission)
    db.session.commit()
    yield permissions
    teardown_db()


@pytest.fixture
def inconsistent_guardians():
    setup_db()
    guardians = get_guardians()
    guardians[1].email = guardians[0].email
    guardians[2].phone_number = guardians[0].phone_number
    yield guardians
    teardown_db()


@pytest.fixture
def inconsistent_permissions():
    setup_db()
    permissions = get_permissions()
    permissions[0].permission_name = permissions[1].permission_name
    yield permissions
    teardown_db()
