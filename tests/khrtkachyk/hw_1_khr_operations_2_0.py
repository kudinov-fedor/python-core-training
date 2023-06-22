import pytest


@pytest.mark.parametrize(["par1", "res"], [
    ((lambda:2 - (5 * 3) ** 2), -223),
    ((lambda:(2 - 5) * 3 ** 2), -27),
    ((lambda:2 - 5 * 3 ** 2), -43),
    ((lambda:pow(5, 2)), 25),
    ((lambda:sum([1, 2, 3])), 6)
])
def test_operators(par1, res):
    assert par1() == res
