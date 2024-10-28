import pytest
from tkupchyn.homework_08.every_person import Person

p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")


@pytest.mark.parametrize('person, expecte_age',
                         (
                                 (p1, 45),
                                 (p2, 28)
                         ))
def test_person_age(person, expecte_age):
    assert person.age == expecte_age


@pytest.mark.parametrize('person, expected_home_address',
                         (
                                 (p1, 'Lives in Vancouver, Canada'),
                                 (p2, 'Lives in Vienna, Austria')
                         ))
def test_person_home(person, expected_home_address):
    assert person.home == expected_home_address


@pytest.mark.parametrize('person, expected_work',
                         (
                                 (p1, 'He is a welder'),
                                 (p2, 'Is a designer')
                         ))
def test_person_work(person, expected_work):
    assert person.work == expected_work


@pytest.mark.parametrize('person, expected_money',
                         (
                                 (p1, '648 000'),
                                 (p2, '56 760')
                         ))
def test_person_work(person, expected_money):
    assert person.money == expected_money
