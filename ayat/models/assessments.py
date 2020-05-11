from ayat.__init__ import db
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSON
import uuid
from ayat.models.users import *

class AssessmentResults(db.Model):
    __tablename__ = 'assessment_results'
    result_id = db.Column(db.Integer, primary_key=True)
    public_assessment_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=False)
    grade = db.Column(db.SMALLINT, nullable=False)

    db.UniqueConstraint(exam_id, student_id, staff_id)
    student = db.relationship("Student")
    exam = db.relationship("Exam")
    staff = db.relationship("Staff")

    def __repr__(self):
        Info_text = f'Grade: {self.grade}\n'

        return Info_text


class Exam(db.Model):
    __tablename__ = 'exam'
    exam_id = db.Column(db.Integer, primary_key=True)
    public_exam_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    question = db.Column(JSON)
    assessment_results = db.relationship("AssessmentResults", back_populates="exam")

    type = db.Column(db.VARCHAR(15))
    __mapper_args__ = {
        'polymorphic_identity': 'exam',
        'polymorphic_on': type
    }

    def __repr__(self):
        Info_text = f'Public ID:{self.public_exam_id}\t'\
                    f'Question: {self.question}\t' \
                    f'Assessment Results: {self.assessment_results}\n'

        return Info_text

    def equals(self,exam):
        if  exam.public_exam_id ==self.public_exam_id:
            return True
        return False

class ProgramExam(Exam):
    __tablename__ = 'program_exam'
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'), unique=True)
    program = db.relationship('Program', backref='program_exam', uselist=False, lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'program_exam'
    }



class CourseExam(Exam):
    __tablename__ = 'course_exam'
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), unique=True)
    course = db.relationship('Course', backref='course_exam', uselist=False, lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'course_exam'
    }



class LessonExam(Exam):
    __tablename__ = 'lesson_exam'
    course_exam_id = db.Column(db.Integer, db.ForeignKey('exam.exam_id'), primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.lesson_id'))
    lesson = db.relationship('Lesson', backref='lesson_exam', uselist=False, lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'lesson_exam'
    }


class ProgramEnrollment(db.Model):
    __tablename__ = 'program_enrollment'
    program_supervision_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'), nullable=False)
    is_accepted = db.Column(db.Boolean, nullable=False, default=False)
    is_completed = db.Column(db.Boolean, nullable=False, default=False)
    join_date = db.Column(db.Date, nullable=False)

    db.UniqueConstraint(student_id, program_id)
    student = db.relationship("Student")
    program = db.relationship("Program")

    def __repr__(self):
        Info_text = f'Is Accepted?: {self.is_accepted}\t' \
                    f'Join Date: {self.join_date}\n'

        return Info_text


class ProgramSupervision(db.Model):
    __tablename__ = 'program_supervision'
    program_supervision_id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.program_id'), nullable=False)

    db.UniqueConstraint(staff_id, program_id)
    staff = db.relationship("Staff")
    program = db.relationship("Program")
