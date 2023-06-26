import pytest


def test_comapre_strings():
    res = ["d", "o", "g"] <= ["d", "a", "y"]
    assert res is False


@pytest.mark.parametrize(["par1", "par2", "res"], [
    (["d", "o", "g"], ["d", "a", "y"], False),
    (["d", "o", "g"], ["d", "a", "y"], False),
    (["d", "o", "g"], ["d", "a", "y"], False),
    (["d", "o", "g"], ["d", "a", "y"], False),
    (["d", "o", "g"], ["d", "a", "y"], False),
    (["d", "o", "g"], ["d", "a", "y"], False),
])
def test_comapre_strings_2(par1, par2, res):
    res = par1 <= par2
    assert res is res
