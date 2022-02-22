import pytest


def test_sum_true1():
    x = 978 + 57
    assert x == 1035


def test_sum_true2():
    a = 57
    b = 793
    assert a + b == 850


def test_sum_true3():
    a = 57
    b = 793
    sum = a + b
    assert sum == 850


def test_sum_true4():
    a = (193, 79, 3957)
    b = sum(a)
    print(b)
    assert b == 4229


def test_sum_true5():
    a = 11
    b = 89
    assert a + b <= 100


@pytest.mark.parametrize('a, b, expected_sum', [
    (35, 91, 126),
    (915, 79, 994),
    (175, 77, 252)
])
def test_sum_parametrize(a, b, expected_sum):
    assert a + b == expected_sum
