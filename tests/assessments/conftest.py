import pytest
from tests.utils.db_utils import teardown_db, setup_db
from tests.utils.assessment_faker import get_program_exam, get_course_exam, get_lesson_exam, get_program_exams
from ayat import db
from tests.users.conftest import student, students, staff, staff_member
from tests.programs.conftest import program, programs


@pytest.fixture
def blank():
    setup_db()
    yield
    teardown_db()


@pytest.fixture
def lesson_exam():
    setup_db()
    lesson_exam = get_lesson_exam()
    db.session.add(lesson_exam)
    db.session.commit()
    yield lesson_exam
    teardown_db()


@pytest.fixture
def course_exam():
    setup_db()
    course_exam = get_course_exam()
    db.session.add(course_exam)
    db.session.commit()
    yield course_exam
    teardown_db()


@pytest.fixture
def program_exam():
    setup_db()
    program_exam = get_program_exam()
    db.session.add(program_exam)
    db.session.commit()
    yield program_exam
    teardown_db()


@pytest.fixture
def inconsistent_exams():
    setup_db()
    program_exams = get_program_exams()
    for program_exam in program_exams:
        db.session.add(program_exam)
    db.session.commit()
    program_exams[0].public_exam_id = program_exams[1].public_exam_id
    yield program_exams
    teardown_db()

@pytest.fixture
def program_exams():
    setup_db()
    program_exams = get_program_exams()
    for program_exam in program_exams:
        db.session.add(program_exam)
    db.session.commit()
    yield program_exams
    teardown_db()