import pytest

from olpopova.homework.homework04.beginning_zeros import beginning_zeros


@pytest.mark.parametrize(['number', 'expected'], [
    ("100", 0),
    ("001", 2),
    ("100100", 0),
    ("001001", 2),
    ("012345679", 1),
    ("0000", 4)
])
def test_function(number, expected):
    assert beginning_zeros(number) == expected
