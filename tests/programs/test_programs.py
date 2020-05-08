"""from ayat.models.programs import Program, Category, Course, Skill, Faq, Lesson, Requirement, Lecture
from ayat import db
from tests.utils.db_utils import check_data_inconsistency
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from tests.utils.program_faker import get_requirement


def test_programs_blank(blank):
    assert [] == Program.query.all()


def test_course_blank(blank):
    assert [] == Course.query.all()


def test_lesson_blank(blank):
    assert [] == Lesson.query.all()


def test_lecture_blank(blank):
    assert [] == Lecture.query.all()


def test_requirement_blank(blank):
    assert [] == Requirement.query.all()


def test_skill_blank(blank):
    assert [] == Skill.query.all()


def test_faq_blank(blank):
    assert [] == Faq.query.all()


def test_category_blank(blank):
    assert [] == Category.query.all()


def test_program_exist(program):
    result = Program.query.first()
    assert program.equals(result)


def test_course_exist(course):
    result = Course.query.first()
    assert course.equals(result)


def test_lesson_exist(lesson):
    result = Lesson.query.first()
    assert lesson.equals(result)


def test_lecture_exist(lecture):
    result = Lecture.query.first()
    assert lecture.equals(result)


def test_skill_exist(skill):
    result = Skill.query.first()
    assert skill.equals(result)


def test_category_exist(category):
    result = Category.query.first()
    assert category.equals(result)


def test_faq_exist(faq):
    result = Faq.query.first()
    assert faq.equals(result)


def test_requirement_exist(requirement):
    result = Requirement.query.first()
    assert requirement.equals(result)


def test_course_uniqueness_inconsistency(inconsistent_courses):
    assert check_data_inconsistency(inconsistent_courses)


def test_lesson_uniqueness_inconsistency(inconsistent_lessons):
    assert check_data_inconsistency(inconsistent_lessons)


def test_lecture_uniqueness_inconsistency(inconsistent_lectures):
    assert check_data_inconsistency(inconsistent_lectures)


def test_category_uniqueness_inconsistency(inconsistent_categories):
    assert check_data_inconsistency(inconsistent_categories)


def test_program_has_courses(program, courses):
    result = False
    for course in courses:
        program.courses.append(course)
    db.session.commit()
    expected_courses = program.courses
    result_program = Program.query.first()
    result_courses = result_program.courses
    for expected_course in expected_courses:
        for result_course in result_courses:
            if expected_course.equals(result_course):
                result = True
                break
    assert result


def test_program_has_lectures(program, lectures):
    result = False
    for lecture in lectures:
        program.lectures.append(lecture)
    db.session.commit()
    expected_lectures = program.lectures
    result_program = Program.query.first()
    result_lectures = result_program.lectures
    for expected_lecture in expected_lectures:
        for result_lecture in result_lectures:
            if expected_lecture.equals(result_lecture):
                result = True
                break
    assert result


def test_course_has_lessons(course, lessons):
    result = False
    for lesson in lessons:
        course.lessons.append(lesson)
    db.session.commit()
    expected_lessons = course.lessons
    result_course = Course.query.first()
    result_lessons = result_course.lessons
    for expected_lesson in expected_lessons:
        for result_lesson in result_lessons:
            if expected_lesson.equals(result_lesson):
                result = True
                break
    assert result


def test_requirement_has_programs(requirement, programs):
    result = False
    for program in programs:
        requirement.program.append(program)
    db.session.commit()
    result_programs = Program.query.all()
    expected_programs = requirement.program
    for expected_program in expected_programs:
        for result_program in result_programs:
            if expected_program.equals(result_program):
                result = True
                break
    assert result


def test_program_has_faqs(programs, faqs):
    result = False
    for program in programs:
        for faq in faqs:
            program.faqs.append(faq)
    db.session.commit()
    result_programs = Program.query.all()
    for program in programs:
        expected_faqs = program.faqs
        for expected_faq in expected_faqs:
            for result_program in result_programs:
                result_faqs = result_program.faqs
                for result_faq in result_faqs:
                    if expected_faq.equals(result_faq):
                        result = True
                        break
    assert result


def test_program_has_skills(programs, skills):
    result = False
    for program in programs:
        for skill in skills:
            program.skills.append(skill)
    db.session.commit()
    result_programs = Program.query.all()
    for program in programs:
        expected_skills = program.skills
        for expected_skill in expected_skills:
            for result_program in result_programs:
                result_skills = result_program.skills
                for result_skill in result_skills:
                    if expected_skill.equals(result_skill):
                        result = True
                        break
    assert result


def test_programs_has_prerequisites(programs):
    result = False
    for program1 in programs:
        for program2 in programs:
            if program1.equals(program2):
                continue
            program1.prerequisites.append(program2)
    db.session.commit()
    result_programs = Program.query.all()
    for program in programs:
        expected_programs = program.prerequisites
        for expected_program in expected_programs:
            for result_program in result_programs:
                if expected_program.equals(result_program):
                    result = True
                    break
    assert result


def test_program_has_categories(programs, categories):
    result = False
    for program in programs:
        for category in categories:
            program.categories.append(category)
    db.session.commit()
    result_programs = Program.query.all()
    for program in programs:
        expected_categories = program.categories
        for expected_category in expected_categories:
            for result_program in result_programs:
                result_categories = result_program.categories
                for result_category in result_categories:
                    if expected_category.equals(result_category):
                        result = True
                        break
    assert result


def test_intermediary_program_skill_uniqueness(program, skill):
    try:
        program.skills.append(skill)
        program.skills.append(skill)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        assert True
    except InvalidRequestError:
        db.session.rollback()
        assert True


def test_intermediary_program_category_uniqueness(program, category):
    try:
        program.categories.append(category)
        program.categories.append(category)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        assert True
    except InvalidRequestError:
        db.session.rollback()
        assert True


def test_intermediary_program_faq_uniqueness(program, faq):
    try:
        program.faqs.append(faq)
        program.faqs.append(faq)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        assert True
    except InvalidRequestError:
        db.session.rollback()
        assert True


def test_intermediary_program_prerequisite_uniqueness(programs):
    try:
        programs[0].prerequisites.append(programs[1])
        programs[0].prerequisites.append(programs[1])
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        assert True
    except InvalidRequestError:
        db.session.rollback()
        assert True"""