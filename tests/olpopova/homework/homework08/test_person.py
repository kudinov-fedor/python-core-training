import pytest

from olpopova.homework.homework08.person import Person


@pytest.fixture
def john():
    return {'first_name': 'John',
            'last_name': 'Smith',
            'birth_date': '19.09.1979',
            'job': 'welder',
            'working_years': 15,
            'salary': 3600,
            'country': 'Canada',
            'city': 'Vancouver',
            'gender': 'male'}


@pytest.fixture
def perceval():
    return {'first_name': 'Perceval',
            'last_name': 'Leclerk',
            'birth_date': '6/1/1997',
            'job': 'F1 Driver',
            'working_years': 10,
            'salary': 1500000,
            'country': 'Monaco',
            'city': 'Monte-Carlo',
            'gender': 'male'}


def test_person(john, perceval):
    p1 = Person(**john)
    p2 = Person(**perceval)
    assert p1.name() == 'John Smith', 'Name'
    assert p1.age() == 44, 'Age'
    assert p2.work() == 'Perceval is a F1 Driver', 'Job'
    assert p1.money() == 'Earned in 15 years - 648 000', 'Money'
    assert p2.home() == 'Lives in Monte-Carlo, Monaco'


def test_person2(perceval):
    p = Person(**perceval)
    assert '.\n'.join([p.name(), p.work(), p.money()]) == \
           '.\n'.join(['Perceval Leclerk', 'Perceval is a F1 Driver', 'Earned in 10 years - 180 000 000'])
