import pytest

from tests.ostetse.Homework3.Fizz import checkio


def test_checkio():
    assert checkio(15) == "Fizz"
    assert checkio(6) == "Fizz"
    assert checkio(10) == "10"
    assert checkio(7) == "7"
