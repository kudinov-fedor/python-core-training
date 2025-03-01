import pytest
from yspryn.hw6.min_max import min_ysp, max_ysp, sorted_bubbles_method, sorted_mim_max_method


def test_min():
    assert min_ysp(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert min_ysp(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1


def test_max():
    assert max_ysp(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert max_ysp(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == -7


@pytest.mark.parametrize("func", [sorted_bubbles_method, sorted_mim_max_method])
def test_sort_bubbles(func):
    assert func(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert func(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert func(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert func(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
