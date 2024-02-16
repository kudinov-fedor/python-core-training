import pytest

from nataliia_romanchuk.homework6.min_max import minnn, sorted_list, maxxx

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


def test_max():
    assert maxxx(0, 1, 2, 3, 4, 5) == max(0, 1, 2, 3, 4, 5)
    assert maxxx(0, 1, 2, 3, 4, 5) == 5
    assert maxxx(*numbers) == max(*numbers)
    assert maxxx(*numbers) == 5
    assert maxxx(*numbers1) == max(*numbers1)
    assert maxxx(*numbers1, key=abs) == 5
    assert maxxx(-8, 0, 1, 2, 3, 4, 5) == max(-8, 0, 1, 2, 3, 4, 5)
    assert maxxx(-8, 0, 1, 2, 3, 4, 5) == 5
    assert maxxx(*numbers2) == max(*numbers2)
    assert maxxx(*numbers2) == 5
    assert maxxx(*numbers2, key=abs) == -8


def test_sorted():
    assert sorted_list(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted_list(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted_list(*numbers) == sorted(numbers)
    assert sorted_list(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted_list(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
