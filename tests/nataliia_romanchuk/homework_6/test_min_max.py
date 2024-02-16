import pytest

from nataliia_romanchuk.homework6.min_max import minnn, min_list, max_list, sorted_list

numbers = [0, 1, 2, 3, 4, 5]
numbers1 = [1, -2, 3, -4, 5]
numbers2 = [-8, 0, 1, 2, 3, 4, 5]


def test_min():
    assert minnn(0, 1, 2, 3, 4, 5) == min(0, 1, 2, 3, 4, 5)
    assert minnn(0, 1, 2, 3, 4, 5) == 0
    assert minnn(*numbers) == min(*numbers)
    assert minnn(*numbers) == 0

    assert minnn(*numbers1) == min(*numbers1)
    assert minnn(*numbers1, key=abs) == 1

    assert minnn(-8, 0, 1, 2, 3, 4, 5) == min(-8, 0, 1, 2, 3, 4, 5)
    assert minnn(-8, 0, 1, 2, 3, 4, 5) == -8
    assert minnn(*numbers2) == min(*numbers2)
    assert minnn(*numbers2) == -8
    assert minnn(*numbers2, key=abs) == 0


def test_min_list():
    assert min_list(0, 1, 2, 3, 4, 5) == min(0, 1, 2, 3, 4, 5)
    assert min_list(0, 1, 2, 3, 4, 5) == 0
    assert min_list(*numbers) == min(*numbers)
    assert min_list(*numbers) == 0
    assert min_list(*numbers1) == min(*numbers1)

    assert min_list(-8, 0, 1, 2, 3, 4, 5) == min(-8, 0, 1, 2, 3, 4, 5)
    assert min_list(-8, 0, 1, 2, 3, 4, 5) == -8
    assert min_list(*numbers2) == min(*numbers2)
    assert min_list(*numbers2) == -8


def test_max_list(*args, key=None):
    assert max_list(0, 1, 2, 3, 4, 5) == max(0, 1, 2, 3, 4, 5)
    assert max_list(0, 1, 2, 3, 4, 5) == 5
    assert max_list(*numbers) == max(*numbers)
    assert max_list(*numbers) == 5
    assert max_list(*numbers1) == max(*numbers1)

    assert max_list(-8, 0, 1, 2, 3, 4, 5) == max(-8, 0, 1, 2, 3, 4, 5)
    assert max_list(-8, 0, 1, 2, 3, 4, 5) == 5
    assert max_list(*numbers2) == max(*numbers2)
    assert max_list(*numbers2) == 5


def test_sorted():
    assert sorted_list(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted_list(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted_list(*numbers) == sorted(numbers)
