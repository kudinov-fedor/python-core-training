import pytest


@pytest.mark.parametrize(["par1", "res"], [
    ([2, 4, -5, 6, -1], [-5, -1, 2, 4, 6]),
    ([2, 6, -5, 4, -1], [-5, -1, 2, 4, 6]),
    ([-1, 4, -5, 6, 2], [-5, -1, 2, 4, 6]),
    ([-5, -1, 2, 4, 6], [-5, -1, 2, 4, 6]),
    ([4, 6, 2, -5, -1], [-5, -1, 2, 4, 6]),
])
def test_comp_lists_sorting(par1, res):
    res = sorted([2, 4, -5, 6, -1], reverse=False)
    assert par1 == res
