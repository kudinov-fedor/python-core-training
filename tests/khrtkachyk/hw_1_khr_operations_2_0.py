import pytest


@pytest.mark.parametrize(["par1", "res"], [
    (2 - (5 * 3) ** 2, 2 - (5 * 3) ** 2),
    (2 - (5 * 3) ** 3, 2 - (5 * 3) ** 2),
    (0, 2 - (5 * 3) ** 2),
    (2 - (5 * 0) ** 2, 2 - (5 * 3) ** 2)
])
def test_operators(par1, res):
    assert par1 == res
