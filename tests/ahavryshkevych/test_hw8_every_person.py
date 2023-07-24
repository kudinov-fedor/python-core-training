import pytest

from ahavryshkevych.every_person import Person


@pytest.fixture
def tested_person1():
    return Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")


def test_person_name(tested_person1):
    assert tested_person1.first_name == "John"


def test_person_lustname(tested_person1):
    assert tested_person1.work() == "He is a welder"


def test_person_total_money(tested_person1):
    assert tested_person1.money() == "648 000"


@pytest.fixture
def tested_person2():
    return Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")


def test_person_salary(tested_person2):
    assert tested_person2.home() == "Lives in Vienna, Austria"
