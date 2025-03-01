import pytest

from olpopova.homework.homework03.max_digit import max_digit


@pytest.mark.parametrize(['value', 'expected'], [
    (0, 0),
    (52, 5),
    (634, 6),
    (1, 1),
    (10000, 1),
    (3579, 9)
])
def test_max_digit(value, expected):
    assert max_digit(value) == expected
