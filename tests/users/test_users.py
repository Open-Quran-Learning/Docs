from ayat.models.users import User, Student, Staff, Guardian
from ayat import db


def test_empty_students(test_student):
    assert [] == Student.query.all()

def test_students_exist(test_student):
    db.session.add(test_student)
    db.session.commit()
    assert test_student in Student.query.all()

def test_staff_exist(test_staff):
    db.session.add(test_staff)
    db.session.commit()
    assert test_staff in Staff.query.all()

#def test_student_have_guardians():
#    db.session.add(self.student)
#    db.session.add(self.guardian)

