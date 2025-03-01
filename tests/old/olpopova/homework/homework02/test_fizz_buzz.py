import pytest

from olpopova.homework.homework02.fizz_buzz import *


@pytest.mark.parametrize(['number', 'expected'], [
    (3, "Fizz"),
    (7, "7"),
    (27, "Fizz"),
    (0, "Fizz")
])
def test_fizz_buzz(number, expected):
    assert checkio(number) == expected


@pytest.mark.parametrize(['number', 'expected'], [
(15, "Fizz Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (7, "7")
])
def test_fizz_buzz_complex(number, expected):
    assert checkio_complex(number) == expected
