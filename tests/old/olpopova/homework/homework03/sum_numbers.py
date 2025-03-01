import pytest

from olpopova.homework.homework03.sum_numbers import *


@pytest.mark.parametrize(['text', 'expected'], [
    ("hi", 0),
    ("who is 1st here", 0),
    ("my numbers is 2", 2),
    ("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year", 3755),
    ("5 plus 6 is", 11),
    ("", 0)
])
def test_sum_numbers(text, expected):
    assert sum_numbers(text) == expected
    assert sum_numbers2(text) == expected
