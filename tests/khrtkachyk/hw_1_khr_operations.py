import pytest


@pytest.mark.parametrize(["par1", "par2", "res"], [
    ([2, 4, -5], [6, -1, 5], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3], [4, 5], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3], [], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])
])
def test_add_sequences(par2, par1, res):
    res = [1, 2, 3] + [4, 5, 6]
    assert par1 + par2 == res
