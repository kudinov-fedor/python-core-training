import pytest

from vpavly.m1.end_zeros import end_zeros_w_loop


# 5 #
@pytest.mark.parametrize('a, expected', [
    (100, 2),
    (0, 1),
    (1, 0)
])
def test_end_zeros(a, expected):
    assert end_zeros_w_loop(a) == expected
