import pytest

from vpavly.m1.replace_first import replace_first


# 9 #
@pytest.mark.parametrize('a, expected', [
    ([1, 2, 3], [2, 3, 1]),
    ([1], [1]), ([], [])
])
def test_replace_first(a, expected):
    assert replace_first(a) == expected
