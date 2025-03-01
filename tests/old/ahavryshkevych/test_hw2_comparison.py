import pytest


def test_compare_tuples():
    res = ("d", "o", "g") > ("d", "a", "y")
    assert res is True


def test_compare_booleans():
    res = (True > False)
    assert res is True


@pytest.mark.parametrize(["par1", "par2", "res"], [
    (["d", "o", "g"], ["d", "a", "y"], True),
    (["dog"], ["day"], True)
])
def test_compare_lists(par1, par2, res):
    result = par1 > par2
    assert result is res


@pytest.mark.parametrize(["par3", "par4", "res4"], [
    ("a", "abc", True),
    ("a", ["a", "b", "c"], True),
    ("z", ["a", "b", "c"], False)
])
def test_compare_string_existence(par3, par4, res4):
    result = par3 in par4
    assert result is res4


def test_compare_str_sorting():
    result = sorted(["banana", "ball", "cat"])
    assert result[0] == "ball"


def test_compare_str_sorting_by_lenght():
    result = sorted(["banana", "ball", "cat"], key=len)
    assert result[0] == "cat"
