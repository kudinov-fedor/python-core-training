def test_math_operations():
    assert 1 + 2 == 3
    assert 3 + 4 == 7
    assert 2 / 4 == 0.5
    assert 2 - 5 * 3 ** 2 == -43
    assert (2 - 5) * 3 ** 2 == -27
    assert abs(-3) == 3
    assert divmod(5, 2) == (2, 1)
    assert sum([1, 2, 3]) == 6
    assert sum((1, 2, 3)) == 6
    assert sum({1, 2, 3}) == 6

    assert (2) * 5 == 10
    assert (2,) * 5 == (2, 2, 2, 2, 2)

    a = (1, 2, 3)
    a + (4, 5, 6)
    assert a == (1, 2, 3)

    a = [1, 2, 3]
    a + [4, 5, 6]
    assert a == [1, 2, 3]

    a = [1, 2, 3]
    b = a + [4, 5, 6]
    assert b == [1, 2, 3, 4, 5, 6]
    assert a == [1, 2, 3]

    a+=[4, 5, 6]
    assert a == [1, 2, 3, 4, 5, 6]
