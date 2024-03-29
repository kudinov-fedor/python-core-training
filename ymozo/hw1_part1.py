import pytest


@pytest.mark.parametrize(["par1", "par2", "res"], [
    (["d", "o", "g"], ["d", "a", "y"], True),
    (["d", "a", "g"], ["d", "o", "y"], False),
    (["a", "b", "c"], ["z", "x", "w"], False),
    ([1, 2], [1, 3], False),
    (["dog"], ["day"], True),
    ([True], [False], True),
    (True, False, True)
])
def test_compare_string(par1, par2, res):
    result = par1 >= par2
    assert result is res


@pytest.mark.parametrize(["par1", "par2", "res"], [
    (True, [1], False),  # list with integer will return False
    (False, [0], False),
    (True, 1, True),  # integer for 1 returns True
    (False, 0, True)  # Integer for 0 returns False
])
def test_check_equality(par1, par2, res):
    result = par1 == par2
    assert result is res


@pytest.mark.parametrize(["par1", "par2", "res"], [
    ("a", ["a", "b", "c"], True),
    ("a", ["abc"], False),
    ("ab", "abc", True),
    ("ab", ["a", "b", "c"], False)
])
def test_check_contains_in(par1, par2, res):
    result = par1 in par2
    assert result is res


@pytest.mark.parametrize(["par1", "par2", "res"], [
    ("z", ["a", "b", "c"], True),
    ("z", "abc", True),
    ("z", ("a", "b", "c"), True),
])
def test_check_contains_not_in(par1, par2, res):
    result = par1 not in par2
    assert result is res


def test_implicit_comparison():
    a = max([2, 3, 1, -2, -5, -8, 12], key=abs)
    assert a == 12, f"a is equal to {a}"


def test_check_srt_max():
    b = max("banana", "ball", "cat", key=len)
    assert b == "banana"


def test_check_reverse():
    a = sorted(["banana", "ball", "cat"], reverse=True, key=len)
    res = ["banana", "ball", "cat"]
    assert a == res
