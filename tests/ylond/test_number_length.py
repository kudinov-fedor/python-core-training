import pytest

from ylond.number_length import number_length


@pytest.mark.parametrize("a, expected", [
    (0, 1),
    (44, 2),
    (5005005005, 10),
    ("", 0)
])
def test_number_length(a, expected):
    assert number_length(a) == expected
