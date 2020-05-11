from ayat.models.users import User, Student, Staff, Guardian, Permission
from ayat import db
from tests.utils.db_utils import check_data_inconsistency
from sqlalchemy.exc import IntegrityError, InvalidRequestError, DataError

"""
def test_students_blank(blank):
    assert [] == Student.query.all()


def test_staff_blank(blank):
    assert [] == Staff.query.all()


def test_permission_blank(blank):
    assert [] == Permission.query.all()


def test_guardian_blank(blank):
    assert [] == Guardian.query.all()


def test_student_has_guardians_blank(student):
    assert [] == student.guardians


def test_students_exist(student):
    result = Student.query.first()
    assert student.equals(result)


def test_staff_exist(staff_member):
    result = Staff.query.first()
    assert staff_member.equals(result)


def test_user_uniqueness_inconsistency(inconsistent_users):
    assert check_data_inconsistency(inconsistent_users)


def test_guardian_uniqueness_inconsistency(inconsistent_guardians):
    assert check_data_inconsistency(inconsistent_guardians)


def test_permissions_uniqueness_inconsistency(inconsistent_permissions):
    assert check_data_inconsistency(inconsistent_permissions)


def test_student_has_guardians(students, guardians):
    result = False
    for student in students:
        for guardian in guardians:
            student.guardians.append(guardian)
    db.session.commit()
    result_students = Student.query.all()
    for student in students:
        expected_guardians = student.guardians
        for expected_guardian in expected_guardians:
            for result_student in result_students:
                result_guardians = result_student.guardians
                for result_guardian in result_guardians:
                    if expected_guardian.equals(result_guardian):
                        result = True
                        break
    assert result


def test_staff_has_permissions(staff, permissions):
    result = False
    for staff_member in staff:
        for permission in permissions:
            staff_member.permissions.append(permission)
    db.session.commit()
    result_staff = Staff.query.all()
    for staff_member in staff:
        expected_permissions = staff_member.permissions
        for expected_permission in expected_permissions:
            for result_staff_member in result_staff:
                result_permissions = result_staff_member.permissions
                for result_permission in result_permissions:
                    if expected_permission.equals(result_permission):
                        result = True
                        break
    assert result


def test_intermediary_student_guardian_uniqueness(student, guardian):
    is_unique = False
    try:
        student.guardians.append(guardian)
        db.session.commit()
        student.guardians.append(guardian)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        is_unique = True
    except InvalidRequestError:
        db.session.rollback()
        is_unique = True
    assert is_unique


def test_intermediary_staff_permission_uniqueness(staff_member, permission):
    is_unique = False
    try:
        staff_member.permissions.append(permission)
        db.session.commit()
        staff_member.permissions.append(permission)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        is_unique = True
    except InvalidRequestError:
        db.session.rollback()
        is_unique = True
    assert is_unique
"""