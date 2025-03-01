from operator import add, mul
from irepela.homework_6.reduce_sum import reduce, sum


def test_reduce():
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce(key=mul, default=1) == 1
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce(key=add, default=0) == 0


def test_sum():
    assert sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8
