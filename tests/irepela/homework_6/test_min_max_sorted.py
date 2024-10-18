import pytest
from irepela.homework_6.min_max import min, max, sorted


@pytest.mark.parametrize("a, b, expected", [
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), None, -7),
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), abs, 1),
    ((-7, -4, -2, -1, -2, -3, -4, -5, -6), abs, -1)
])
def test_min(a, b, expected):
    assert min(a, key=b) == expected


@pytest.mark.parametrize("a, b, expected", [
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), None, 6),
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), abs, -7)
])
def test_max(a, b, expected):
    assert max(a, key=b) == expected


@pytest.mark.parametrize("a, b, c, expected", [
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), None, False, [-7, -4, -2, 1, 2, 3, 4, 5, 6]),
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), abs, False, [1, -2, 2, 3, -4, 4, 5, 6, -7]),
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), None, True, [6, 5, 4, 3, 2, 1, -2, -4, -7]),
    ((-7, -4, -2, 1, 2, 3, 4, 5, 6), abs, True, [-7, 6, 5, -4, 4, 3, -2, 2, 1]),
])
def test_sorted(a, b, c, expected):
    assert sorted(a, key=b, reverse=c) == expected
