from ayat.models.programs import Program, Category, Course, Skill, Faq, Lesson, Requirement, Lecture
import datetime


def get_program():
    requirement_id = get_requirement()
    d0 = datetime.datetime(year=2020, month=3, day=7)
    d1 = datetime.datetime(year=2020, month=5, day=7)
    program = Program(program_name='hadst', difficulty_level='easy', price=0, program_picture='a.png',
                      program_cover='b.png'
                      , program_description='faded', is_available=True, start_date=d0, end_date=d1,
                      is_open_to_public=True)
    requirement_id.program.append(program)
    return program


def get_programs():
    requirement_id = get_requirement()
    d0 = datetime.datetime(year=2020, month=3, day=1)
    d1 = datetime.datetime(year=2020, month=4, day=1)
    d3 = datetime.datetime(year=2020, month=5, day=1)
    d4 = datetime.datetime(year=2020, month=6, day=1)
    d5 = datetime.datetime(year=2021, month=1, day=1)
    d6 = datetime.datetime(year=2021, month=2, day=1)
    program_list = [Program(program_name='first', difficulty_level='easy', price=0, program_picture='a.png',
                            program_cover='b.png'
                            , program_description='faded', is_available=True, start_date=d0, end_date=d1,
                            is_open_to_public=False),
                    Program(program_name='second', difficulty_level='hard', price=0, program_picture='a.png',
                            program_cover='b.png'
                            , program_description='faded', is_available=True, start_date=d0, end_date=d1,
                            is_open_to_public=False)]
    requirement_id.program.append(program_list[0])
    requirement_id.program.append(program_list[1])
    return program_list


def get_course():
    program = get_program()
    course = Course(course_name='course1',
                    course_description='about',
                    course_order=1)
    program.courses.append(course)
    return course


def get_courses():
    program = get_program()
    course_list = [Course(course_name='course1',
                          course_description='about',
                          course_order=1),
                   Course(course_name='course2',
                          course_order=2)]
    program.courses.append(course_list[0])
    program.courses.append(course_list[1])
    return course_list


def get_lesson():
    program = get_program()
    course = get_course()
    program.courses.append(course)
    lesson = Lesson(lesson_name='lesson1',
                    lesson_description='about',
                    lesson_order=1,
                    content='sds',
                    is_unlocked=True)
    course.lessons.append(lesson)
    return lesson


def get_lessons():
    program = get_program()
    course = get_course()
    lesson_list = [Lesson(lesson_name='lesson1',
                          lesson_description='about',
                          lesson_order=1,
                          content='a:a, ',
                          is_unlocked=True),
                   Lesson(lesson_name='lesson2',
                          content='a:a, ',
                          lesson_order=2,
                          is_unlocked=False)]
    program.courses.append(course)
    course.lessons.append(lesson_list[0])
    course.lessons.append(lesson_list[1])
    return lesson_list


def get_lecture():
    program = get_program()
    lecture = Lecture(lecture_name='lec1',
                      lecture_description='about',
                      lecture_order=1,
                      content='a',
                      is_unlocked=True)
    program.lectures.append(lecture)
    return lecture


def get_lectures():
    program = get_program()
    lecture_list = [Lecture(lecture_name='lec1',
                            lecture_description='about',
                            lecture_order=1,
                            content='sdad.com',
                            is_unlocked=True),
                    Lecture(lecture_name='lec2',
                            lecture_order=2,
                            content='sss.com',
                            is_unlocked=False)]
    program.lectures.append(lecture_list[0])
    program.lectures.append(lecture_list[1])
    return lecture_list


def get_skill():
    skill = Skill(skill_name='good')
    return skill


def get_skills():
    skill_list = [Skill(skill_name='good'),
                  Skill(skill_name='good brdo')]
    return skill_list


def get_faq():
    faq = Faq(question='why?',
              answer='kda')
    return faq


def get_faqs():
    faq_list = [Faq(question='why?', answer='kda'),
                Faq(question='what?', answer='ay7aga')]
    return faq_list


def get_requirement():
    requirement = Requirement(min_age=15, max_age=60, gender=True)
    return requirement


def get_requirements():
    requirement_list = [Requirement(min_age=15, max_age=60, gender=True),
                        Requirement(min_age=18, max_age=75, gender=False)]
    return requirement_list


def get_category():
    category = Category(category_name='islamic')
    return category


def get_categories():
    category_list = [Category(category_name='islamic'),
                     Category(category_name='education')]
    return category_list

