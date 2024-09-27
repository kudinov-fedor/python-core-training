import pytest
from irepela.homework_2.sum_numbers import sum_numbers, sum_numbers_comprehension


@pytest.mark.parametrize("arg, expected", [
    ("hi", 0),
    ("who is 1st here", 0),
    ("my numbers is 2", 2),
    ("5 plus 6 is", 11),
    ("", 0),
    ("his picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year", 3755)
])
def test_sum_numbers(arg, expected):
    assert sum_numbers(arg) == expected


@pytest.mark.parametrize("arg, expected", [
    ("hi", 0),
    ("who is 1st here", 0),
    ("my numbers is 2", 2),
    ("5 plus 6 is", 11),
    ("", 0),
    ("his picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year", 3755)
])
def test_sum_numbers_comprehension(arg, expected):
    assert sum_numbers_comprehension(arg) == expected
