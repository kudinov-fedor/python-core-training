import pytest
from akaiafiuk.backward_string import backward_string, backward_string_using_reversed


@pytest.mark.parametrize("value, expected", [
    ("val", "lav"),
    ("", ""),
    ("ohho", "ohho"),
    ("123456789", "987654321")
])
def test_backward_string(value, expected):
    assert backward_string(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("val", "lav"),
    ("", ""),
    ("ohho", "ohho"),
    ("123456789", "987654321")
])
def test_backward_string_using_reversed(value, expected):
    assert backward_string_using_reversed(value) == expected
