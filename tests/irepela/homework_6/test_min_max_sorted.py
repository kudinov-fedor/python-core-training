from irepela.homework_6.min_max import min, max, sorted


def test_min():
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert min(-7, -4, -2, -1, -2, -3, -4, -5, -6, key=abs) == -1


def test_max():
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == -7


def test_sorted():
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
