import pytest

from dyurchen.max_digit import max_digit


@pytest.mark.parametrize("input_param, expected", [
    (0, 0),
    (52, 5),
    (634, 6),
    (1, 1),
    (10000, 1)
])
def test_max_digit(input_param, expected):
    assert max_digit(input_param) == expected
