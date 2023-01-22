import pytest
from tlazu.Backward_string import backward_string


@pytest.mark.parametrize("value, result", [
    ("123456789", "987654321"),
    ("val", "lav"),
    ("", "")
])
def test_backward_string(value, result):
    assert backward_string(value) == result