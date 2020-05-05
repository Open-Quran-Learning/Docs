from ayat.models.users import User, Student, Staff, Guardian, Permission
from ayat import db
from tests.utils.db_utils import check_data_consistency
from sqlalchemy.exc import IntegrityError, InvalidRequestError, DataError


def test_students_blank(blank):
    assert [] == Student.query.all()


def test_staff_blank(blank):
    assert [] == Staff.query.all()


def test_permission_blank(blank):
    assert [] == Permission.query.all()


def test_guardian_blank(blank):
    assert [] == Guardian.query.all()


def test_students_has_guardians_blank(student):
    db.session.add(student)
    db.session.commit()
    assert [] == student.guardians


def test_students_exist(student):
    result = Student.query.first()
    assert student.equals(result)


def test_staff_exist(staff_member):
    result = Staff.query.first()
    assert staff_member.equals(result)


def test_user_uniqueness_inconsistency(inconsistent_users):
    assert check_data_consistency(inconsistent_users)


def test_guardian_uniqueness_inconsistency(inconsistent_guardians):
    assert check_data_consistency(inconsistent_guardians)


def test_permissions_uniqueness_inconsistency(inconsistent_permissions):
    assert check_data_consistency(inconsistent_permissions)


def test_student_has_guardians(students, guardians):
    result = False
    for student in students:
        for guardian in guardians:
            student.guardians.append(guardian)
    db.session.commit()
    students = Student.query.all()
    for student in students:
        expected_guardians = student.guardians
        for guardian in student.guardians:
            for expected_guardian in expected_guardians:
                if guardian.equals(expected_guardian):
                    result = True
                    break
    assert result


def test_staff_has_permissions(staff, permissions):
    result = False
    for staff_member in staff:
        for permission in permissions:
            staff_member.permissions.append(permission)
    db.session.commit()
    staff = Staff.query.all()
    for staff_member in staff:
        expected_permissions = staff_member.permissions
        for permission in staff_member.permissions:
            for expected_permission in expected_permissions:
                if permission.equals(expected_permission):
                    result = True
                    break
    assert result


def test_intermediary_student_guardian_uniqueness(student, guardian):
    try:
        student.guardians.append(guardian)
        student.guardians.append(guardian)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        assert True
    except InvalidRequestError:
        db.session.rollback()
        assert True


def test_intermediary_staff_permission_uniqueness(staff_member, permission):
    try:
        staff_member.permissions.append(permission)
        staff_member.permissions.append(permission)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        assert True
    except InvalidRequestError:
        db.session.rollback()
        assert True
