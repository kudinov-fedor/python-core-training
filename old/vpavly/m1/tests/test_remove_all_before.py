import pytest

from vpavly.m1.remove_all_before import remove_all_before


# 7 #
@pytest.mark.parametrize('a, b, expected', [
    ([1, 2, 3, 4, 5], 4, [4, 5])
])
def test_remove_all_before(a, b, expected):
    assert list(remove_all_before(a, b)) == expected
