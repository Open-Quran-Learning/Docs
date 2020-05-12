from ayat import db
from ayat.models import *
from tests.utils.user_faker import *
from tests.utils.program_faker import *
from tests.utils.db_utils import *
from tests.utils.assessment_faker import *

student = get_student()
staff_member = get_staff_member()
program = get_program()
db.session.add(student)
db.session.add(staff_member)
db.session.add(program)
db.session.commit()

program_enrollment = ProgramEnrollment(student = student, program = program, join_date = datetime.date(year=2020,month=5,day=1))
db.session.add(program_enrollment)
db.session.commit()


program_supervision = ProgramSupervision(staff = staff_member, program = program)
db.session.add(program_supervision)
db.session.commit()

program_exam = get_program_exam()
db.session.add(program_exam)
db.session.commit()

course_exam = get_course_exam()
db.session.add(course_exam)
db.session.commit()

lesson_exam = get_lesson_exam()
db.session.add(lesson_exam)
db.session.commit()


web_address = WebAddress(url = "https://www.google.com")
lecture_schedule = LectureSchedule(recurrent = True, online = True)
appointment = Appointment(day=2, start_hour=datetime.time(3,30), end_hour=datetime.time(5,30), schedule=lecture_schedule, event_address=web_address)