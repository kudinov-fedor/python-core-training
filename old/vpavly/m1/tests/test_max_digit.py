import pytest

from vpavly.m1.max_digit import max_digit


# 10 #
@pytest.mark.parametrize('a, expected', [
    (123, 3),
    (1, 1),
    (1000, 1)
])
def test_max_digit(a, expected):
    assert max_digit(a) == expected
