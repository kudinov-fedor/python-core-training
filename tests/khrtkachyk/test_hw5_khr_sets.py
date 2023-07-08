import pytest


@pytest.mark.parametrize("par1, par2, res", [
    ({"a", "b", "x"}, {"a", "x", "f"}, {"b"}),
    ({"a", "b", "x"}, {""}, {"a", "b", "x"}),
    ({""}, {1, 2, 3}, {""})
])
def test_sets(par1, par2, res):
    """
    Return set of items that only exist in set "par1", and not in set "par2"
    """
    assert par1.difference(par2) == res


@pytest.mark.parametrize("par1, par2, res", [
    ({"a", "b", "x"}, {"a", "x", "f"}, {"b", "f"}),
    ({"a", "b", "x"}, {""}, {"a", "b", "x", ""}),
    ({1}, {"1abc"}, {"1abc", 1})
])
def test_sets_2(par1, par2, res):
    """
    Return set that contains all unique items from both sets
    """
    assert par1.symmetric_difference(par2) == res
    assert par1 ^ par2 == res


@pytest.mark.parametrize("par1, par2, res", [
    ({"a", "b", "c"}, {"b", "x", "d"}, {"a", "b", "c", "d", "x"}),
    ({"ab", "c", "d"}, {(1, 2, 3), ""}, {"ab", "c", "d", "", (1, 2, 3)})
])
def test_set3(par1, par2, res):
    """
    Check sets updating functionality
    """
    par1.update(par2)
    assert par1 == res
