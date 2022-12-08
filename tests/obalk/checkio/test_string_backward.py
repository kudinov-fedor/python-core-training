import pytest
from obalk.checkio.string_backward import backward_string


@pytest.mark.parametrize("value, result", [
    ("123456789", "987654321"),
    ("val", "lav"),
    ("", "")
])
def test_backward_string(value, result):
    assert backward_string(value) == result
