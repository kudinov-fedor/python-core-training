import pytest

from vpavly.m1.begin_zeros import beginning_zeros_w_int


# 8 #
@pytest.mark.parametrize('a, expected', [
    ('001', 2),
    ('0', 1),
    ('', 0)
])
def test_begin_zeros(a, expected):
    assert beginning_zeros_w_int(a) == expected
