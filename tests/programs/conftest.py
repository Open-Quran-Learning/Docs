import pytest
from tests.utils.db_utils import teardown_db, setup_db
from tests.utils.program_faker import get_program, get_course, get_lesson, get_lecture, get_skill, \
    get_category, get_faq, get_requirement, get_programs, get_courses, get_lessons, get_lectures, \
    get_skills, get_categories, get_faqs, get_requirements
from ayat import db


@pytest.fixture
def blank():
    setup_db()
    yield
    teardown_db()


@pytest.fixture
def program():
    setup_db()
    program = get_program()
    db.session.add(program)
    db.session.commit()
    yield program
    teardown_db()


@pytest.fixture
def programs():
    setup_db()
    programs = get_programs()
    for program in programs:
        db.session.add(program)
    db.session.commit()
    yield programs
    teardown_db()


@pytest.fixture
def prerequisites():
    setup_db()
    programs = get_programs()
    for program in programs:
        db.session.add(program)
    db.session.commit()
    yield programs
    teardown_db()


@pytest.fixture
def course():
    setup_db()
    course = get_course()
    db.session.add(course)
    db.session.commit()
    yield course
    teardown_db()


@pytest.fixture
def courses():
    setup_db()
    courses = get_courses()
    for course in courses:
        db.session.add(course)
    db.session.commit()
    yield courses
    teardown_db()


@pytest.fixture
def inconsistent_courses():
    setup_db()
    courses = get_courses()
    courses[1].course_order = courses[0].course_order
    courses[1].program_id = courses[0].program_id
    yield courses
    teardown_db()


@pytest.fixture
def lesson():
    setup_db()
    lesson = get_lesson()
    db.session.add(lesson)
    db.session.commit()
    yield lesson
    teardown_db()


@pytest.fixture
def lessons():
    setup_db()
    lessons = get_lessons()
    for lesson in lessons:
        db.session.add(lesson)
    db.session.commit()
    yield lessons
    teardown_db()


@pytest.fixture
def inconsistent_lessons():
    setup_db()
    lessons = get_lessons()
    lessons[1].lesson_order = lessons[0].lesson_order
    lessons[1].course_id = lessons[0].course_id
    yield lessons
    teardown_db()


@pytest.fixture
def lecture():
    setup_db()
    lecture = get_lecture()
    db.session.add(lecture)
    db.session.commit()
    yield lecture
    teardown_db()


@pytest.fixture
def lectures():
    setup_db()
    lectures = get_lectures()
    for lecture in lectures:
        db.session.add(lecture)
    db.session.commit()
    yield lectures
    teardown_db()


@pytest.fixture
def inconsistent_lectures():
    setup_db()
    lectures = get_lectures()
    lectures[1].lecture_order = lectures[0].lecture_order
    lectures[1].program_id = lectures[0].program_id
    yield lectures
    teardown_db()


@pytest.fixture
def skill():
    setup_db()
    skill = get_skill()
    db.session.add(skill)
    db.session.commit()
    yield skill
    teardown_db()


@pytest.fixture
def skills():
    setup_db()
    skills = get_skills()
    for skill in skills:
        db.session.add(skill)
    db.session.commit()
    yield skills
    teardown_db()


@pytest.fixture
def category():
    setup_db()
    category = get_category()
    db.session.add(category)
    db.session.commit()
    yield category
    teardown_db()


@pytest.fixture
def inconsistent_categories():
    setup_db()
    categories = get_categories()
    categories[1].category_name = categories[0].category_name
    yield categories
    teardown_db()


@pytest.fixture
def categories():
    setup_db()
    categories = get_categories()
    for category in categories:
        db.session.add(category)
    db.session.commit()
    yield categories
    teardown_db()


@pytest.fixture
def faq():
    setup_db()
    faq = get_faq()
    db.session.add(faq)
    db.session.commit()
    yield faq
    teardown_db()


@pytest.fixture
def faqs():
    setup_db()
    faqs = get_faqs()
    for faq in faqs:
        db.session.add(faq)
    db.session.commit()
    yield faqs
    teardown_db()


@pytest.fixture
def requirement():
    setup_db()
    requirement = get_requirement()
    db.session.add(requirement)
    db.session.commit()
    yield requirement
    teardown_db()


@pytest.fixture
def requirements():
    setup_db()
    requirements = get_requirements()
    for requirement in requirements:
        db.session.add(requirement)
    db.session.commit()
    yield requirements
    teardown_db()
