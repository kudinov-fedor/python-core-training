import pytest


def test_max():
    assert max((2, 3, 1, -2, -5, -8, -12), key=abs) == -12


def test_abs():
    assert abs(-12) != -12


def test_compare_tuples1():
    assert (1, 2 + 2, 3) == (1, 4, 3)


def test_compare_tuples2():
    assert ((1, 2) > (1, 1, 1, 1))


def test_sets_comparison():
    assert {1, 2, 3, 4} == {1, 2, 3, 4}


def test_sets_comparison1():
    a = {1, 2, 3, 4}
    b = {1, 2, 3, 4}
    assert a is not b


def test_lists_comparison():
    assert [1, 2, 3, 4] == [1, 2, 3, 4]


def test_lists_comparison1():
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    assert a is not b


def test_sum():
    assert sum({1, 2, 3}) == 6


def test_sum1():
    assert sum({0, 0, }) == 0
