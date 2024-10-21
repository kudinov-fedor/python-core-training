import pytest
from irepela.homework_7.caching import fibo


@pytest.mark.parametrize("a, expected", [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (6, 13),
    (7, 21),
    (8, 34),
    (9, 55),
])
def test_chain_sum(a, expected):
    assert fibo(a) == expected
