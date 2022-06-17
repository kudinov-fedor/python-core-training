import pytest


def test_abs():
    res = abs(-5)
    assert res == 5


def test_tuple():
    res = tuple('abc')
    assert res == ('a', 'b', 'c')


# noinspection PyUnreachableCode
def test_reversed():
    test_list = ['dasasd', 'asdsa', 1, 22]
    test_list.reverse()
    assert test_list == [22, 1, 'asdsa', 'dasasd']


def test_len():
    res = 'bajada'
    assert len(res) == 6


# HOW TO MAKE VIA PARAMETRIZED ???

# @pytest.mark.parametrize('val1, val2, total', [
#     [11, 22, 33],  # positive numbers PASS
#     [11, 22, 0],  # positive numbers FAIL
#     [-13, -15, -28]  # negative numbers PASS
# ])
# def test_sum(val1, val2, total):
#     assert total == sum(val1, val2)


def test_sum():
    a = [1, 3, 4]
    assert 8 == sum(a)
