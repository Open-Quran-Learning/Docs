from ayat import db
from sqlalchemy.exc import IntegrityError, InvalidRequestError, DataError


def setup_db():
    """Method used to build a database"""
    print("Building DB...")
    db.create_all()


def teardown_db():
    """Method used to destroy a database"""
    print("Destroying DB...")
    db.session.remove()
    db.drop_all()
    db.session.bind.dispose()


def clean_db():
    """Method used to truncate all tables in a database"""
    for table in reversed(db.metadata.sorted_tables):
        print('Clear table %s' % table)
        db.session.execute(table.delete())


def clean_user():
    """Method used to truncate all tables in user model"""
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        if table.name in ['user', 'staff', 'student', 'guardian', 'permission']:
            print('Clear table %s' % table)
            db.session.execute(table.delete())
    db.session.commit()


def reset_db():
    teardown_db()
    setup_db()


def check_data_inconsistency(entity):
    is_inconsistent = False

    for row in entity:
        db.session.add(row)
    try:
        db.session.commit()
    except InvalidRequestError:
        db.session.rollback()
        is_inconsistent = True
    except IntegrityError:
        db.session.rollback()
        is_inconsistent = True
    except DataError:
        db.session.rollback()
        is_inconsistent = True
    return is_inconsistent
