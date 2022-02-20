import pytest


def test_min_true1():
    a = [59, 745, 9, -3, 91]
    res = min(a)
    assert res == -3


def test_min_true2():
    b = [12, 71, 0, 51, 264]
    res = min(b)
    assert res == 0


def test_min_false():
    c = [93, 4325, -135, 71, 39]
    res = min(c)
    assert res == 39


@pytest.mark.parametrize('item, expected_min', [
    ([59, 745, 9, -3, 91], -3),
    ([12, 71, 0, 51, 264], 0),
    ([93, 4325, -135, 71, 39], -135)
])
def test_min_parametrize(item, expected_min):
    a = item
    res = min(a)
    assert res == expected_min
