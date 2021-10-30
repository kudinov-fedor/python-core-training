from akaiafiuk.multiply import multiply_two
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 6),
    (2, 2, 4),
    (1, 0, 0)
])
def test_multiply_two(a, b, expected):
    assert multiply_two(a, b) == expected