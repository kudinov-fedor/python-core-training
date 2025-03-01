import pytest

import hw8_persons


@pytest.fixture()
def person1():
    return hw8_persons.Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")


@pytest.fixture
def person2():
    return hw8_persons.Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")


def test_person1(person1):
    assert person1.name() == "John Smith", "Name"
    assert person1.age() == 38, "Age"
    assert person1.money() == "648 000", "Money"
    assert person1.home() == "Lives in Vancouver, Canada", "Home"
    assert person1.work() == "Is a welder", "Job"


def test_person2_full_name(person2):
    full_name = person2.name()
    assert full_name == "Hanna Rose May", "Name"


def test_person2_age(person2):
    person_age = person2.age()
    assert person_age == 22, "Age"


def test_person2_home(person2):
    person_home = person2.home()
    assert person_home == "Lives in Vienna, Austria", "Home"


def test_person2_money(person2):
    total_rewards = person2.money()
    assert total_rewards == "56 760.0", "Money"


def test_person2_work(person2):
    person_work = person2.work()
    assert person_work == "Is a designer", "Job"
