import pytest

from olpopova.homework.homework06.min_max_sorted import min, max, sorted, identify_insert_index


def test_min():
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert min(-7, 4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1


def test_max():
    assert max(-7, 4, -2, 6, key=abs) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6


def test_sorted():
    assert sorted(6, 1, -2, -4, -7) == [-7, -4, -2, 1, 6]
    assert sorted(-1, 122, 9, 7, 56, 0) == [-1, 0, 7, 9, 56, 122]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, 4, -4, 3, 2, -2, 1]


@pytest.mark.parametrize("data, item, res", [
    ([], 5, 0),
    ([1], 5, 1),
    ([6], 5, 0),
    ([3, 4], 1, 0),
    ([3, 6], 5, 1),
    ([3, 4], 5, 2),
])
@pytest.mark.parametrize("key", [
    (lambda i: i), None,
])
def test_inserts(data, item, res, key):
    assert identify_insert_index(data, item, key=key) == res
