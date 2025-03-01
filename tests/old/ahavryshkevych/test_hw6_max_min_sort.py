import pytest

from ahavryshkevych.taks_hw6_min_max_reverse import own_sort, own_min, own_max


def test_own_min():
    assert own_min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert own_min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1


def test_own_max():
    assert own_max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert own_max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6


@pytest.mark.parametrize(["initial_list", "reverse", "key", "result"], [
    ([-7, -4, -2, 1, 2, 3, 4, 5, 6], False, None, [-7, -4, -2, 1, 2, 3, 4, 5, 6]),
    ([-7, -4, -2, 1, 2, 3, 4, 5, 6], True, None, [6, 5, 4, 3, 2, 1, -2, -4, -7]),
    ([-7, -4, -2, 1, 2, 3, 4, 5, 6], False, abs, [1, -2, 2, 3, -4, 4, 5, 6, -7]),
    ([-7, -4, -2, 1, 2, 3, 4, 5, 6], True, abs, [-7, 6, 5, -4, 4, 3, -2, 2, 1]),
],
)
def test_sort_func(initial_list, reverse, key, result):
    assert own_sort(*initial_list, reverse=reverse, key=key) == result
