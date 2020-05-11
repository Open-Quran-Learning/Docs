from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ayat import db
from sqlalchemy import UniqueConstraint

program_skill = db.Table('program_skill', db.Model.metadata,
                         db.Column('program_skill_id', db.Integer, primary_key=True),
                         db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')),
                         db.Column('skill_id', db.SMALLINT, db.ForeignKey('skill.skill_id')),
                         UniqueConstraint('program_id', 'skill_id'))

program_faqs = db.Table('program_faqs', db.Model.metadata,
                        db.Column('program_faq_id', db.SMALLINT, primary_key=True),
                        db.Column('faq_id', db.Integer, db.ForeignKey('faq.faq_id')),
                        db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')),
                        UniqueConstraint('program_id', 'faq_id'))

program_category = db.Table('program_category', db.Model.metadata,
                            db.Column('program_category_id', db.SMALLINT, primary_key=True),
                            db.Column('category_id', db.Integer, db.ForeignKey('category.category_id')),
                            db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')),
                            UniqueConstraint('program_id', 'category_id'))

program_prerequisite = db.Table('program_prerequisite', db.Model.metadata,
                                db.Column('prerequisite_id', db.SMALLINT, primary_key=True),
                                db.Column('dependency_id', db.Integer, db.ForeignKey('program.program_id')),
                                db.Column('program_id', db.Integer, db.ForeignKey('program.program_id')),
                                UniqueConstraint('program_id', 'dependency_id'))

############################################################################
class Program(db.Model):
    __tablename__ = "program"
    program_id = db.Column(db.SMALLINT, primary_key=True)
    public_program_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    program_name = db.Column(db.VARCHAR(60), nullable=False)
    difficulty_level = db.Column(db.VARCHAR(30), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    program_picture = db.Column(db.VARCHAR(20), nullable=False)
    is_open_to_public = db.Column(db.Boolean, nullable=False)
    program_cover = db.Column(db.VARCHAR(20), nullable=False)
    program_description = db.Column(db.VARCHAR(255), nullable=False)
    is_available = db.Column(db.Boolean, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    requirement_id = db.Column(db.SMALLINT, db.ForeignKey("requirement.requirement_id"), nullable=False)
    skills = db.relationship('Skill', secondary=program_skill, backref=db.backref('program', lazy='dynamic'))
    faqs = db.relationship('Faq', secondary=program_faqs, backref=db.backref('program', lazy='dynamic'))
    categories = db.relationship('Category', secondary=program_category, backref=db.backref('program', lazy='dynamic'))
    courses = db.relationship('Course', backref=db.backref('program'))
    lectures = db.relationship('Lecture', backref=db.backref('program'))
    requirements = db.relationship("Requirement", backref=db.backref('program'))
    program_enrollment = db.relationship("ProgramEnrollment", back_populates="program")
    staff = db.relationship('ProgramSupervision', back_populates="program")
    prerequisites = db.relationship(
        'Program',
        secondary=program_prerequisite,
        primaryjoin=program_id == program_prerequisite.c.program_id,
        secondaryjoin=program_id == program_prerequisite.c.dependency_id,
        backref=db.backref('program_prerequisite')
    )

    def __repr__(self):
        info_text = (f'program id: {self.program_id}.\t'
                     f'public program id: {self.public_program_id}.\t'
                     f'program name: {self.program_name}.\t'
                     f'difficulty level: {self.difficulty_level}.\t'
                     f'price: {self.price}.\t'
                     f'program_picture: {self.program_picture}.\t'
                     f'program cover: {self.program_cover}.\t'
                     f'program description: {self.program_description}.\t'
                     f'price: {self.price}.\t'
                     f'available: {self.is_available}.\t'
                     f'start date: {self.start_date}.\t'
                     f'end date: {self.end_date}.\t'
                     f'requirement id: {self.requirement_id}.\n')

        return info_text

    def equals(self, program):
        if self.program_name == program.program_name \
                and self.difficulty_level == program.difficulty_level \
                and self.price == program.price \
                and self.program_picture == program.program_picture \
                and self.is_open_to_public == program.is_open_to_public \
                and self.program_cover == program.program_cover \
                and self.program_description == program.program_description \
                and self.is_available == program.is_available \
                and self.start_date == program.start_date \
                and self.end_date == program.end_date \
                and self.requirement_id == program.requirement_id:
            return True
        return False


class Skill(db.Model):
    __tablename__ = "skill"
    skill_id = db.Column(db.SMALLINT, primary_key=True)
    skill_name = db.Column(db.VARCHAR(30), nullable=False)

    def __repr__(self):
        info_text = (f'skill id: {self.skill_id}.\t'
                     f'skill name: {self.skill_name}.\n')

        return info_text

    def equals(self, skill):
        if self.skill_name == skill.skill_name:
            return True
        return False


class Faq(db.Model):
    __tablename__ = "faq"
    faq_id = db.Column(db.SMALLINT, primary_key=True, unique=True)
    question = db.Column(db.VARCHAR(255), nullable=False)
    answer = db.Column(db.VARCHAR(255), nullable=False)

    def __repr__(self):
        info_text = (f'faq id: {self.faq_id}.\t'
                     f'question: {self.question}.\t'
                     f'answer: {self.answer}.\n')

        return info_text

    def equals(self, faq):
        if self.question == faq.question and self.answer == faq.answer:
            return True
        return False


class Course(db.Model):
    __tablename__ = "course"
    __table_args__ = (db.UniqueConstraint('program_id', 'course_order'),)
    course_id = db.Column(db.SMALLINT, primary_key=True)
    public_course_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    program_id = db.Column(db.SMALLINT, db.ForeignKey("program.program_id"), nullable=False)
    course_name = db.Column(db.VARCHAR(60), nullable=False)
    course_description = db.Column(db.VARCHAR(255))  # may be deleted
    course_order = db.Column(db.SMALLINT, nullable=False)
    lessons = db.relationship('Lesson', backref=db.backref('course'))

    def __repr__(self):
        info_text = (f'course id: {self.course_id}.\t'
                     f'public course id: {self.public_course_id}.\t'
                     f'program id: {self.program_id}.\t'
                     f'course name: {self.course_name}.\t'
                     f'course description: {self.course_description}.\t'
                     f'course order: {self.course_order}.\n')
        return info_text

    def equals(self, course):
        if self.course_name == course.course_name \
                and self.course_description == course.course_description \
                and self.course_order == course.course_order \
                and self.program_id == course.program_id:
            return True
        return False


class Lesson(db.Model):
    __tablename__ = "lesson"
    __table_args__ = (db.UniqueConstraint('course_id', 'lesson_order'),)
    lesson_id = db.Column(db.SMALLINT, primary_key=True)
    public_lesson_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    course_id = db.Column(db.SMALLINT, db.ForeignKey("course.course_id"), nullable=False)
    lesson_name = db.Column(db.VARCHAR(60), nullable=False)
    lesson_description = db.Column(db.VARCHAR(255))  # may be deleted
    content = db.Column(db.JSON, nullable=False)
    lesson_order = db.Column(db.SMALLINT, nullable=False)
    is_unlocked = db.Column(db.BOOLEAN, default=True)

    def __repr__(self):
        info_text = (f'lesson id: {self.lesson_id}.\t'
                     f'public lesson id: {self.public_lesson_id}.\t'
                     f'course id: {self.course_id}.\t'
                     f'lesson name: {self.lesson_name}.\t'
                     f'lesson_description: {self.lesson_description}.\t'
                     f'content: {self.content}.\t'
                     f'lesson order: {self.lesson_order}.\t'
                     f'lesson description: {self.lesson_description}.\t'
                     f'is unlocked: {self.is_unlocked}.\n')
        return info_text

    def equals(self, lesson):
        if self.lesson_name == lesson.lesson_name \
                and self.course_id == lesson.course_id \
                and self.lesson_description == lesson.lesson_description \
                and self.content == lesson.content \
                and self.lesson_order == lesson.lesson_order \
                and self.is_unlocked == lesson.is_unlocked:
            return True
        return False


class Requirement(db.Model):
    __tablename__ = "requirement"
    requirement_id = db.Column(db.SMALLINT, primary_key=True)
    min_age = db.Column(db.SMALLINT, nullable=False)
    max_age = db.Column(db.SMALLINT, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        info_text = (f'requirement id: {self.requirement_id}.\t'
                     f'min age: {self.min_age}.\t'
                     f'max age: {self.max_age}.\t'
                     f'gender: {self.gender}.\n')
        return info_text

    def equals(self, requirement):
        if self.min_age == requirement.min_age \
                and self.max_age == requirement.max_age \
                and self.gender == requirement.gender:
            return True
        return False


class Category(db.Model):
    __tablename__ = "category"
    category_id = db.Column(db.SMALLINT, primary_key=True)
    category_name = db.Column(db.VARCHAR(30), unique=True)

    def __repr__(self):
        info_text = (f'category id: {self.category_id}.\t'
                     f'category name: {self.category_name}.\n')
        return info_text

    def equals(self, category):
        if self.category_name == category.category_name:
            return True
        return False


class Lecture(db.Model):
    __tablename__ = "lecture"
    __table_args__ = (db.UniqueConstraint('program_id', 'lecture_order'),)
    lecture_id = db.Column(db.SMALLINT, primary_key=True)
    public_lecture_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    lecture_name = db.Column(db.VARCHAR(60), nullable=False)
    program_id = db.Column(db.SMALLINT, db.ForeignKey("program.program_id"), nullable=False)
    lecture_description = db.Column(db.VARCHAR(255))  # may be deleted
    content = db.Column(db.VARCHAR(60), nullable=False)
    lecture_order = db.Column(db.SMALLINT, nullable=False)
    is_unlocked = db.Column(db.BOOLEAN, default=True)

    def __repr__(self):
        info_text = (f'lecture id: {self.lecture_id}.\t'
                     f'public lecture id: {self.public_lecture_id}.\t'
                     f'lecture name: {self.lecture_name}.\t'
                     f'program id: {self.program_id}.\t'
                     f'lesson description: {self.lecture_description}.\t'
                     f'content: {self.content}.\t'
                     f'lecture order: {self.lecture_order}.\t'
                     f'is unlocked: {self.is_unlocked}.\n')
        return info_text

    def equals(self, lecture):
        if self.lecture_name == lecture.lecture_name \
                and self.lecture_description == lecture.lecture_description \
                and self.content == lecture.content \
                and self.lecture_order == lecture.lecture_order \
                and self.is_unlocked == lecture.is_unlocked:
            return True
        return False
