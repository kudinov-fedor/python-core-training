import pytest

from olpopova.homework.homework02.backward_string import *


@pytest.mark.parametrize(['string', 'expected'], [
    ("val", "lav"),
    ("", ""),
    ("ohho", "ohho"),
    ("123456789", "987654321")
])
def test_backward_string(string, expected):
    assert backward_string(string) == backward_string2(string) == expected
