import pytest

from olpopova.homework.homework05 import exceptions


@pytest.mark.parametrize(['first_value', 'invalid_value'], [
    (6, 0),
    (6, 'f')
])
def test_zero_division_error(first_value, invalid_value):
    exceptions.division_error(first_value, invalid_value)


@pytest.mark.parametrize(['first_value', 'second_value'], [
    (6, 0),
    (6, 'f')
])
def test_raise_error(first_value, second_value):
    exceptions.raise_error(first_value, second_value)
