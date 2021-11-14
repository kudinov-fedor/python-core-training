import pytest

from vpavly.m1.nearest_value import nearest_value


# 12 #
@pytest.mark.parametrize('a, b, expected', [
    ([4, 7, 10, 11, 12, 17], 9, 10),
    ([4, 7, 10, 11, 12, 17], 8, 7),
    ([4, 8, 10, 11, 12, 17], 9, 8),
    ([-1, 2, 3], 0, -1)])
def test_nearest_value(a, b, expected):
    assert nearest_value(a, b) == expected
