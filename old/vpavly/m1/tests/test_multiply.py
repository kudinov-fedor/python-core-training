import pytest

from vpavly.m1.multiply import mult_two


# 1 #
@pytest.mark.parametrize('a, b, expected', [
    (10, 5, 50),
    (5, 2, 10),
    (-4, 2, -8),
    (0, 5, 0)
])
def test_mult_two(a, b, expected):
    assert mult_two(a, b) == expected
