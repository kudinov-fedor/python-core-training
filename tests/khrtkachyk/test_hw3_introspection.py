import pytest


@pytest.mark.parametrize(["par", "par0", "res0"], [
    ((1, 2, 3), (1, 2, 3), True),
    (id((1, 2, 3)), id((1, 2, 3)), True),
    ([1, 2, 3], [1, 2, 3], True),
    (id([1, 2, 3]), id([1, 2, 3]), False)
])
def test_equality(par, par0, res0):
    assert (par == par0) is res0


@pytest.mark.parametrize(["par1", "par2", "res1"], [
    (lambda: (1, 2, 3), lambda: (1, 2, 3), True),
    (lambda: ([1, 2], [3, 4]), lambda: ([1, 2], [3, 4]), False)
])
def test_identity(par1, par2, res1):
    assert (par1() is par2()) is res1


@pytest.mark.parametrize(["n", "res"], [
    (3, "<class 'generator'>")
])
def test_yield_numbers(n, res):
    start_num = 0
    while start_num < n:
        yield start_num
        start_num += 1
    assert (test_yield_numbers(n)).__class__ == res
