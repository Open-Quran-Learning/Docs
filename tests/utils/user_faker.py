from ayat.models.users import Student, Staff, Guardian, Permission
import datetime


def get_student():
    student = Student(name='Mohamed',
                      email='mohamed@gmail.com',
                      birth_date=datetime.date(year=1996, month=10, day=17),
                      country_name='Egypt',
                      phone_number='01897779788',
                      gender=True,
                      password='daskjsldsaj',
                      registration_date=datetime.date(year=2020, month=5, day=10),
                      type='student'
                      )
    return student


def get_students():
    student_list = [Student(name='Mohamed',
                            email='mohamed@gmail.com',
                            birth_date=datetime.date(year=1990, month=5, day=1),
                            country_name='Egypt',
                            phone_number='01897779788',
                            gender=True,
                            password='daskjsldsaj',
                            registration_date=datetime.date(year=2020, month=5, day=10),
                            type='student'
                            ),
                    Student(name='Khaled',
                            email='khaled@gmail.com',
                            birth_date=datetime.date(year=1994, month=1, day=1),
                            country_name='Egypt',
                            phone_number='01897771518',
                            gender=True,
                            password='daskjsldsaj',
                            registration_date=datetime.date(year=2020, month=5, day=12),
                            type='student'
                            ),
                    Student(name='Mahmoud',
                            email='mohmoud@gmail.com',
                            birth_date=datetime.date(year=1996, month=10, day=17),
                            country_name='Egypt',
                            phone_number='01895644788',
                            gender=True,
                            password='daskjsldsaj',
                            is_activated=True,
                            registration_date=datetime.date(year=2020, month=5, day=10),
                            type='student'
                            )
                    ]
    return student_list


def get_staff_member():
    staff = Staff(name='Mohamed',
                  email='mohamed@gmail.com',
                  birth_date=datetime.date(year=1986, month=1, day=7),
                  country_name='Egypt',
                  phone_number='01897779788',
                  gender=True,
                  password='daskjsldsaj',
                  registration_date=datetime.date(year=2020, month=5, day=10),
                  type='staff'
                  )
    return staff


def get_staff():
    staff_list = [Staff(name='Hazem',
                        email='hazem@gmail.com',
                        birth_date=datetime.date(year=1986, month=1, day=7),
                        country_name='Egypt',
                        phone_number='01551846648',
                        gender=True,
                        password='daskjsldsaj',
                        registration_date=datetime.date(year=2020, month=5, day=10),
                        type='staff'
                        ),
                  Staff(name='Sattar',
                        email='sattar@gmail.com',
                        birth_date=datetime.date(year=1986, month=1, day=7),
                        country_name='Egypt',
                        phone_number='01468466648',
                        gender=True,
                        password='daskjsldsaj',
                        registration_date=datetime.date(year=2020, month=5, day=10),
                        type='staff'
                        ),
                  Staff(name='youssef',
                        email='youssef@gmail.com',
                        birth_date=datetime.date(year=1986, month=1, day=7),
                        country_name='Egypt',
                        phone_number='01558796648',
                        gender=True,
                        password='daskjsldsaj',
                        registration_date=datetime.date(year=2020, month=5, day=10),
                        type='staff'
                        )
                  ]
    return staff_list


def get_guardian():
    guardian = Guardian(
        email='mohamed@gmail.com',
        phone_number='01897779788',
    )
    return guardian


def get_guardians():
    guardian_list = [Guardian(email='mohamed@gmail.com',
                              phone_number='01897779788'
                              ),
                     Guardian(email='mahmoud@gmail.com',
                              phone_number='01894549788'
                              ),
                     Guardian(email='khaled@gmail.com',
                              phone_number='018947849788'
                              )
                     ]
    return guardian_list


def get_permission():
    permission = Permission(permission_name="Administrator")
    return permission


def get_permissions():
    permission_list = [Permission(permission_name="Program_Supervisor"),
                       Permission(permission_name="Administrator"),
                       ]
    return permission_list
