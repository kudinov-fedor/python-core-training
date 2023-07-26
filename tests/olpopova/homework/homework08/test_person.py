import datetime

import pytest

from olpopova.homework.homework08.person import Person


@pytest.fixture
def john():
    return {'first_name': 'John',
            'last_name': 'Smith',
            'birth_date': datetime.date(1979, 9, 19),
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
            'birth_date': datetime.date(1997, 10, 16),
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
    assert p2.work() == 'Is a F1 Driver', 'Job'
    assert p1.money() == '648 000', 'Money'
    assert p2.home() == 'Lives in Monte-Carlo, Monaco'
