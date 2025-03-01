import pytest
from tkupchyn.homework_08.every_person import Person


@pytest.fixture
def create_pesrons():
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    return p1, p2


def test_person_age(create_pesrons):
    assert create_pesrons[0].age == 45
    assert create_pesrons[1].age == 28


def test_person_home(create_pesrons):
    assert create_pesrons[0].home == 'Lives in Vancouver, Canada'
    assert create_pesrons[1].home == 'Lives in Vienna, Austria'


def test_person_work(create_pesrons):
    assert create_pesrons[0].work == 'He is a welder'
    assert create_pesrons[1].work == 'Is a designer'


def test_person_money(create_pesrons):
    assert create_pesrons[0].money == '648 000'
    assert create_pesrons[1].money == '56 760'
