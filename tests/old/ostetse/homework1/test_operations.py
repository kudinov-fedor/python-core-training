import pytest


def test_operations():
    assert (1 + 2) == 3
    assert (2 / 4) == 0.5
    assert (2 - 5 * 3 ** 2) == -43
    assert ((2 - 5) * 3 ** 2)
    assert (2 - (5 * 3) ** 2)
    assert (5 / 2) == 2.5
    assert (5 // 2) == 2
    assert (5 % 2) == 1
    assert abs(-3) == 3
    assert divmod(5, 2) == (2, 1)
    assert pow(5, 2) == 25
    assert round(4.345, 2) == 4.34
    assert round(4.345) == 4
    assert round(4.345, 1) == 4.3
    assert sum([1, 2, 3]) == 6
    assert sum((1, 2, 3)) == 6
    assert sum({1, 2, 3}) == 6

    # operations on sequences
    assert ("abc" + "efg") == "abcefg"
    assert ("abc" * 2) == "abcabc"
    assert ((2) * 5) == 10
    assert ((2,) * 5) == (2, 2, 2, 2, 2)
    assert ((1, 2, 3) + (4, 5, 6)) == (1, 2, 3, 4, 5, 6)

    assert ([1, 2, 3] + [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert ([1, 2] * 3) == [1, 2, 1, 2, 1, 2]
