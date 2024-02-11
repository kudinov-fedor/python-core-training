from operator import add, mul

from yspryn.hw6.reduce_sum import reduce, sum


def test_reduce_func():
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce(key=mul, default=1) == 1
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce(key=add, default=0) == 0


def test_sum_func():
    assert sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8