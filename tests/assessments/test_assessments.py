from ayat.models.assessments import Exam, ProgramExam, CourseExam, LessonExam, AssessmentResults, ProgramEnrollment, \
    ProgramSupervision
from ayat import db
from tests.utils.db_utils import check_data_inconsistency
from sqlalchemy.exc import IntegrityError, InvalidRequestError, DataError
import datetime
from ayat.models.users import Student, Staff
from ayat.models.programs import Program


def test_program_exam_blank(blank):
    assert [] == ProgramExam.query.all()


def test_course_exam_blank(blank):
    assert [] == LessonExam.query.all()


def test_lesson_exam_blank(blank):
    assert [] == LessonExam.query.all()


def test_lesson_exam_has_exams(lesson_exam):
    result = LessonExam.query.first()
    assert lesson_exam.equals(result)


def test_course_exam_has_exams(course_exam):
    result = CourseExam.query.first()
    assert course_exam.equals(result)


def test_program_exam_has_exams(program_exam):
    result = ProgramExam.query.first()
    assert program_exam.equals(result)


def test_exam_uniqueness_inconsistency(inconsistent_exams):
    assert check_data_inconsistency(inconsistent_exams)


def test_program_enrollment_has_students_enrolled_in_programs(students, programs):
    result = False
    for student in students:
        for program in programs:
            program_enrollment = ProgramEnrollment(student=student, program=program,
                                                   join_date=datetime.date(year=2020, month=5, day=1))
            db.session.add(program_enrollment)
    db.session.commit()
    result_students = Student.query.all()
    for student in students:
        expected_programs = []
        for i in range(0, len(student.program_enrollment)):
            for program in programs:
                if student.program_enrollment[i].program_id == program.program_id:
                    expected_programs.append(program)
        for expected_program in expected_programs:
            for result_student in result_students:
                result_programs = []
                for i in range(0, len(result_student.program_enrollment)):
                    result_programs.append(
                        Program.query.filter_by(program_id=result_student.program_enrollment[i].program_id).first())
                for result_program in result_programs:
                    if expected_program.equals(result_program):
                        result = True
                        break
    assert result


def test_program_enrollment_inconsistency(student, program):
    is_unique = False
    try:
        program_enrollment = ProgramEnrollment(student=student, program=program,
                                               join_date=datetime.date(year=2020, month=5, day=1))
        db.session.add(program_enrollment)
        db.session.commit()
        program_enrollment = ProgramEnrollment(student=student, program=program,
                                               join_date=datetime.date(year=2020, month=5, day=1))
        db.session.add(program_enrollment)
        db.session.commit()
    except IntegrityError:
        is_unique = True
        db.session.rollback()
    except InvalidRequestError:
        is_unique = True
        db.session.rollback()
    assert is_unique


def test_program_supervision_has_staff_managing_programs(staff, programs):
    result = False
    for staff_member in staff:
        for program in programs:
            program_supervision = ProgramSupervision(staff=staff_member, program=program)
            db.session.add(program_supervision)
    db.session.commit()
    result_staff = Staff.query.all()
    for staff_member in staff:
        expected_programs = []
        for i in range(0, len(staff_member.program_supervision)):
            for program in programs:
                if staff_member.program_supervision[i].program_id == program.program_id:
                    expected_programs.append(program)
        for expected_program in expected_programs:
            for result_staff_member in result_staff:
                result_programs = []
                for i in range(0, len(result_staff_member.program_supervision)):
                    result_programs.append(
                        Program.query.filter_by(
                            program_id=result_staff_member.program_supervision[i].program_id).first())
                for result_program in result_programs:
                    if expected_program.equals(result_program):
                        result = True
                        break
    assert result


def test_program_supervision_inconsistency(staff_member, program):
    is_unique = False
    try:
        program_supervision = ProgramSupervision(staff=staff_member, program=program)
        db.session.add(program_supervision)
        db.session.commit()
        program_supervision = ProgramSupervision(staff=staff_member, program=program)
        db.session.add(program_supervision)
        db.session.commit()
    except IntegrityError:
        is_unique = True
        db.session.rollback()
    except InvalidRequestError:
        is_unique = True
        db.session.rollback()
    assert is_unique
