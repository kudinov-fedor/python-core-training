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


@pytest.fixture
def third_person():
    return Person("cat",
            "cat",
            "14.08.1998",
            "vendor",
            7,
            4000,
            "UK",
            "London",
            "unknown")


def test_name_function(first_person, second_person, third_person):
    assert first_person.name() == "John Smith"
    assert second_person.name() == "Ana Maria Sad"
    assert third_person.name() == "cat cat"


def test_age_function(first_person, second_person, third_person):
    assert first_person.age() == 44
    assert second_person.age() == 24
    assert third_person.age() == 25


def test_work_function(first_person, second_person, third_person):
    assert first_person.work() == "He is a welder"
    assert second_person.work() == "She is a designer"
    assert third_person.work() == "Is a vendor"


def test_money_function(first_person, second_person, third_person):
    assert first_person.money() == '648 000'
    assert second_person.money() == '86 400'
    assert third_person.money() == '336 000'


def test_home_function(first_person, second_person, third_person):
    assert first_person.home() == 'Lives in Vancouver, Canada'
    assert second_person.home() == 'Lives in Kyiv, Ukraine'
    assert third_person.home() == 'Lives in London, UK'
