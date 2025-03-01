import pytest

from yspryn.checkio_tasks.reverse_string_hw5 import backward_string, backward_string2


@pytest.mark.parametrize("string, res", [
    ("val", "lav"),
    ("", ""),
    ("ohho", "ohho"),
    ("123456789", "987654321")
])
def test_reverse_string(string, res):
    assert backward_string(string) == res


@pytest.mark.parametrize("string, res", [
    ("val", "lav"),
    ("", ""),
    ("ohho", "ohho"),
    ("123456789", "987654321")
])
def test_reverse_string2(string, res):
    assert backward_string2(string) == res
