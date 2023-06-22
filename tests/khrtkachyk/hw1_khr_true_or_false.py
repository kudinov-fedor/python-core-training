import pytest


@pytest.mark.parametrize(["par1", "res"], [
    ((lambda: len([False, ]) > 0), True),
    ((lambda: len({1, "abc"}) > 0), True),
    ((lambda: bool({})), False),
    ((lambda: len([False, ]) == 0), False),
    ((lambda: not (1, 2, 3)), False),
    ((lambda: "it is true" if [None] else "it is false"), "it is true"),
    ((lambda: True and False), False),
    ((lambda: True or False), True)
])
def test_true_false(par1, res):
    assert par1() is res
