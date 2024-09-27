import pytest


def mult_two(a: int, b: int):
    return a * b


@pytest.mark.parametrize('a,b, result', [
    (0, 1, 0),
    (1, 2, 2),
    (3, 4, 12),
    (5, 6, 30),
    (7, 8, 56)])
def test_mult_two(a, b, result):
    assert mult_two(a, b) == result
