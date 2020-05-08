from tests.utils.program_faker import *
from tests.utils.db_utils import *
programs = get_programs()
for program in programs:
	db.session.add(program)
db.session.commit()