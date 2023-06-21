import pytest


@pytest.mark.parametrize(["par1", "res"], [
    (2 - (5 * 3) ^ 2, -15),
    (2 - (5 * 3) ^ 3, -15),
    (0, -15),
    (2 - (5 * 0) ^ 2, -15)
])
def test_xor(par1, res):
    res = 2 - (5 * 3) ^ 2
    assert par1 == res
