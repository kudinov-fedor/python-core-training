import pytest
from math import ceil, floor, pow, sqrt, fmod


@pytest.mark.math
@pytest.mark.parametrize("a, b, expected", [
    (4.4, 2, 3),
    (3, 2, 2),
    (11, 2, 6)
])
def test_ceil_func(a, b, expected):
    assert ceil(a / b) == expected


@pytest.mark.math
@pytest.mark.parametrize("a, b, expected", [
    (4.4, 2, 8),
    (5.5, 3, 16),
    (6.6, 4, 26)
])
def test_floor_func(a, b, expected):
    assert floor(a * b) == expected


@pytest.mark.math
@pytest.mark.parametrize("a, b, expected", [
    (3, 3, 27),
    (4, 4, 256)
])
def test_pow_func(a, b, expected):
    assert pow(a, b) == expected


@pytest.mark.math
@pytest.mark.parametrize("num, expected", [
    (144, 12),
    (9, 3)
])
def test_sqrt_func(num, expected):
    assert sqrt(num) == expected


@pytest.mark.math
@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 1),
    (7, 2, 1)
])
def test_fmod(a, b, expected):
    assert fmod(a, b) == expected
