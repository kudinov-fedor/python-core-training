import random

import pytest

"""
Tests for type() python built-in function
"""


@pytest.mark.parametrize("data,res", [
    (type(5), int),
    (type(5.0), float),
    (type(True), bool),
    (type("Hello"), str),
    (type([1, 2, 3]), list),
    (type(("apple", "banana", "cherry")), tuple),
    (type({"brand": "Ford", "model": "Mustang", "year": 1964}), dict),
    (type(1j), complex),
    (type(int(abs(-100.05))), int)
])
def test_check_type_of_data(data, res):
    assert data == res


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
    except Exception as err:
        print('Handling run-time error:', err.__class__)
        assert type(err) == ZeroDivisionError
        assert type(err) != ArithmeticError
