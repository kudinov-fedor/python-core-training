import random

import pytest

"""
Tests for type() python built-in function
"""


@pytest.mark.parametrize("data,res", [
    (5, int),
    (5.0, float),
    (True, bool),
    ("Hello", str),
    ([1, 2, 3], list),
    (("apple", "banana", "cherry"), tuple),
    ({"brand": "Ford", "model": "Mustang", "year": 1964}, dict),
    (1j, complex),
    (int(abs(-100.05)), int)
])
def test_check_type_of_data(data, res):
    assert type(data) == res


@pytest.mark.smoke
def test_not_include_in():
    assert 5 in [5 / 5, 10 / 2, 7]


def test_check_random():
    x = random.randint(0, 100)
    assert 0 <= x <= 100


"""
Tests for handling ZeroDivisionError
"""


def test_zero_division_error():
    try:
        1 / 0
    except ZeroDivisionError as err:
        print('Handling run-time error:', type(err))
    else:
        raise AssertionError("Expected Error never risen")
