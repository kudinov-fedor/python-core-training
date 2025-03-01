import pytest


@pytest.mark.parametrize(["par1", "res"], [
    ("banana", "cat"),
    ("ball", "cat"),
    ("cat", "cat"),
])
def test_compare_len(par1, res):
    res = min("banana", "ball", "cat", key=len)
    if par1 == res:
        assert par1 == res
    else:
        raise AssertionError(f'"{res}" is shorter than "{par1}"')
