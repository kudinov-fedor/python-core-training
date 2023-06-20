import pytest


@pytest.mark.parametrize(["par1", "par2", "res"], [
    ("dog", "day", True),  # alphabet order
    ((1, 2), (1, 3), False),
    (True, False, True)  # True == 1, False == 0
])
def test_comparison(par1, par2, res):
    result = par1 > par2
    assert result is res


def test_identity():
    a = []  # id 4485558784
    b = a  # id 4485558784
    c = []  # new created object, id 4485403264
    assert a is b
    assert a is not c
    assert a == b
    assert a == c


@pytest.mark.parametrize(["param", "key", "y"], [
    ([2, 3, 1, -2, -5, -8, 12], abs, 12),
    ([2, 3, 1, -2, -5, -80, 12], abs, -80)  # abs = absolute value, -+ doesn't matter
])
def test_max(param, key, y):
    x = max(param, key=key)  # how to fix this "Unexpected type" warning?
    assert x == y
