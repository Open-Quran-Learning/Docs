from ayat.models.assessments import Exam, ProgramExam, CourseExam, LessonExam, AssessmentResults, ProgramEnrollment, \
    ProgramSupervision
from tests.utils.program_faker import get_program, get_programs, get_course, get_lesson


def get_program_exam():
    program = get_program()
    program_exam = ProgramExam(question=[{
        "questionTitle": "bla bla bla",
        "order": 3,
        "mark": 1,
        "answers": [{
            "A": "bla bla bla",
            "B": "bla bla bla",
            "C": "bla bla bla",
            "D": "bla bla bla",
            "answer": "A"
        }]
    }], type='program_exam')
    program.program_exam.append(program_exam)
    return program_exam


def get_program_exams():
    programs = get_programs()
    program_exams = [ProgramExam(question=[{
        "questionTitle": "bla bla bla",
        "order": 3,
        "mark": 1,
        "answers": [{
            "A": "bla bla bla",
            "B": "bla bla bla",
            "C": "bla bla bla",
            "D": "bla bla bla",
            "answer": "A"
        }]
    }], type='program_exam'),
        ProgramExam(question=[{
            "questionTitle": "bla bla bla",
            "order": 3,
            "mark": 1,
            "answers": [{
                "A": "bla bla bla",
                "B": "bla bla bla",
                "C": "bla bla bla",
                "D": "bla bla bla",
                "answer": "A"
            }]
        }], type='program_exam')
    ]
    if len(programs) <= len(program_exams):
        for i in range(0, len(programs)):
            programs[i].program_exam.append(program_exams[i])
    else:
        for i in range(0, len(program_exams)):
            programs[i].program_exam.append(program_exams[i])
    return program_exams

def get_course_exam():
    course = get_course()
    course_exam = CourseExam(question=[{
        "questionTitle": "bla bla bla",
        "order": 3,
        "mark": 1,
        "answers": [{
            "A": "bla bla bla",
            "B": "bla bla bla",
            "C": "bla bla bla",
            "D": "bla bla bla",
            "answer": "A"
        }]
    }], type='course_exam')
    course.course_exam.append(course_exam)
    return course_exam


def get_lesson_exam():
    lesson = get_lesson()
    lesson_exam = LessonExam(question=[{
        "questionTitle": "bla bla bla",
        "order": 3,
        "mark": 1,
        "answers": [{
            "A": "bla bla bla",
            "B": "bla bla bla",
            "C": "bla bla bla",
            "D": "bla bla bla",
            "answer": "A"
        }]
    }], type='lesson_exam')
    lesson.lesson_exam.append(lesson_exam)
    return lesson_exam

