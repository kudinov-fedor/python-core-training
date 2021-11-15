import pytest

from vpavly.m1.check_even import check_even


# 15 #
@pytest.mark.parametrize('a, expected', [
    (-2, True),
    (9999, False),
    (0, True)
])
def test_check_even(a, expected):
    assert check_even(a) == expected
