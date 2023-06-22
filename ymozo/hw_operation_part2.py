import pytest


def test_check_multiplication():
    res = 2 - 5 * 3 ** 2
    expected = -43
    assert res == expected


def test_check_multiplication_1():
    res = (2 - 5) * 3 ** 2
    expected = -27
    assert res == expected


def test_check_multiplication_2():
    res = 2 - (5 * 3) ** 2
    expected = -223
    assert res == expected


def test_check_absolute():
    assert abs(-3) == 3


def test_check_round():
    assert round(4.345, 2) == 4.34


def test_check_pow():
    assert pow(5, 2) == 25


def test_check_sum():
    assert sum([1, 2, 3]) == 6


def test_check_sum_1():
    assert sum({1, 2, 3}) == 6


def test_check_modulo_operation():
    a = 7 % 3
    res = 1
    assert a == res


def test_check_division_int():
    a = 9 // 2
    res = 4
    assert a == res

# region sequences
def test_check_sequences_1():
    seq = "abc" + "efg"
    result = "abcefg"
    assert seq == result


def test_check_sequences_2():
    seq = "abc" * 2
    result = "abcabc"
    assert seq == result


def test_check_sequences_3():
    seq = (2) * 5
    result = 10
    assert seq == result


def test_check_sequences_4():
    seq = (2, ) * 5
    result = (2, 2, 2, 2, 2)
    assert seq == result


def test_check_sequences_5():
    seq = (1, 2, 3) + (4, 5, 6)
    result = (1, 2, 3, 4, 5, 6)
    assert seq == result


def test_check_sequences_6():
    seq = [1, 2, 3] + [4, 5, 6]
    result = [1, 2, 3, 4, 5, 6]
    assert seq == result


def test_check_sequences_7():
    seq = [1, 2] * 3
    result = [1, 2, 1, 2, 1, 2]
    assert seq == result
# endregion
