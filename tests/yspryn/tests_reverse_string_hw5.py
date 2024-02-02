import pytest

from yspryn.checkio_tasks.reverse_string_hw5 import backward_string


@pytest.mark.parametrize("string, res", [
    ("val", "lav"),
    ("", ""),
    ("ohho", "ohho"),
    ("123456789", "987654321")
])
def test_reverse_string(string, res):
    assert backward_string(string) == res
