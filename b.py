from tests.utils.program_faker import *
from tests.utils.db_utils import *
programs = get_programs()
programs[0].prerequisites.append(programs[1])
db.session.add(programs[0])
db.session.add(programs[1])
db.session.commit()