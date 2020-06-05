# Open Quran Learning Project Data

OQLP Data is the database repository where all the database models , implementation and documentation reside.

## Download

1- Download Open Quran Learning Data code from: 
https://github.com/Open-Quran-Learning/Data.git

2- In a terminal window, navigate into your Data directory.

3- Install all dependencies using the command below:
```cmd
pip3 install -r requirements.txt
```

## Development
1- setup your desired DBMS example: postgresql-12. <br>
2- Set the following enviroment variables, you can find the DATABASE_URIs in the SQLAlchemy documentation, for example:
```cmd
export DATABASE_URI="postgresql://rolename:password@host:port/database"
```

## Documentation
- [Terminology][]
- [Entity Definition][]
- [Users Model][]
- [Address Model][]
- [Programs][]
- [Program Enrollment][]
- [Program Supervision][]
- [Scheduling][]
- [Exam Models][]

[Terminology]: ./docs/terminology.md
[Entity Definition]: ./docs/entity-definition.md
[Users Model]: ./docs/users-model.md
[Address Model]: ./docs/address-model.md
[Programs]: ./docs/program-model.md
[Program Enrollment]: ./docs/program-enrollment.md
[Program Supervision]: ./docs/program-supervision-model.md
[Scheduling]: ./docs/scheduling-model.md
[Exam Models]: ./docs/exam-models.md
