from anmykh.homework.homework_8_persons import Person
import pytest


@pytest.fixture
def first_person():
    return Person("John",
           "Smith",
           "19.09.1979",
           "welder",
           15,
           3600,
           "Canada",
           "Vancouver",
           "male")


@pytest.fixture
def second_person():
    return Person("Ana Maria",
            "Sad",
            "28.01.2000",
            "designer",
            6,
            1200,
            "Ukraine",
            "Kyiv",
            "female")


def test_name_function(first_person, second_person):
    assert first_person.name() == "John Smith"
    assert second_person.name() == "Ana Maria Sad"


def test_age_function(first_person, second_person):
    assert first_person.age() == 44
    assert second_person.age() == 24


def test_work_function(first_person, second_person):
    assert first_person.work() == "He is a welder"
    assert second_person.work() == "She is a designer"


def test_money_function(first_person, second_person):
    assert first_person.money() == '648 000'
    assert second_person.money() == '86 400'


def test_home_function(first_person, second_person):
    assert first_person.home() == 'Lives in Vancouver, Canada'
    assert second_person.home() == 'Lives in Kyiv, Ukraine'
