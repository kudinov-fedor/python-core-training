import pytest

from vpavly.m1.number_length import number_length


# 4 #
@pytest.mark.parametrize('a, expected', [
    (10, 2),
    (1, 1),
    (987654, 6)
])
def test_number_length(a, expected):
    assert number_length(a) == expected
