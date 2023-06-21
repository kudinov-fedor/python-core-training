import pytest


@pytest.mark.parametrize(["par1", "par2", "res"], [
    ([2, 4, -5], [6, -1, 5], [1, 2, 3] + [4, 5, 6]),
    ([1, 2, 3], [4, 5], [1, 2, 3] + [4, 5, 6]),
    ([1, 2, 3], [], [1, 2, 3] + [4, 5, 6]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3] + [4, 5, 6])
])
def test_add_sequences(par1, par2, res):
    assert par1 + par2 == res
