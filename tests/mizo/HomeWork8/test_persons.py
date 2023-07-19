from datetime import datetime
from mizo.task_persons import Person


def test_person1_name():
    person1_date_of_birth = datetime(1979, 9, 19)
    person1 = Person('John', 'Smith', person1_date_of_birth, 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
    assert person1.name() == 'John Smith'


def test_person2_name():
    person2_date_of_birth = datetime(1995, 12, 5)
    person2 = Person('Hanna Rose', 'May', person2_date_of_birth, 'designer', 2.2, 2150, 'Austria', 'Vienna', 'unknown')
    assert person2.name() == 'Hanna Rose May'


def test_person1_job():
    person1_date_of_birth = datetime(1979, 9, 19)
    person1 = Person('John', 'Smith', person1_date_of_birth, 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
    assert person1.job() == 'welder'


def test_person2_job():
    person2_date_of_birth = datetime(1995, 12, 5)
    person2 = Person('Hanna Rose', 'May', person2_date_of_birth, 'designer', 2.2, 2150, 'Austria', 'Vienna', 'unknown')
    assert person2.job() == 'designer'


def test_person1_age():
    person1_date_of_birth = datetime(1979, 9, 19)
    person1 = Person('John', 'Smith', person1_date_of_birth, 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
    assert person1.age() == 38


def test_person2_age():
    person2_date_of_birth = datetime(1995, 12, 5)
    person2 = Person('Hanna Rose', 'May', person2_date_of_birth, 'designer', 2.2, 2150, 'Austria', 'Vienna', 'unknown')
    assert person2.age() == 22


def test_person1_money():
    person1_date_of_birth = datetime(1979, 9, 19)
    person1 = Person('John', 'Smith', person1_date_of_birth, 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
    assert person1.money() == 54000


def test_person2_money():
    person2_date_of_birth = datetime(1995, 12, 5)
    person2 = Person('Hanna Rose', 'May', person2_date_of_birth, 'designer', 2.2, 2150, 'Austria', 'Vienna', 'unknown')
    assert person2.money() == 4730
