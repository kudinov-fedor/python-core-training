import pytest

from odysh.max_digit import max_digit


@pytest.mark.parametrize("number, max", [
    (123, 3),
    (456, 6),
    (654, 6),
    (421, 4)
])
def test_max_digit(number, max):
    assert max_digit(number) == max


def test_negative_max_digit():
    assert max_digit(123) == 2


def test_negative_str_to_max_digit():
    assert max_digit("123") == 3
