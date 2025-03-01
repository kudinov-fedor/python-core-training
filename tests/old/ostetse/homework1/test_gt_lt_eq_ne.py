import pytest


@pytest.mark.parametrize(
    ["a", "b", "res"],
    [
        ["dog", "day", True],
        [(1, 2), (1, 3), False],
        [("d", "o", "g"), ("d", "a", "y"), True]
    ])
def test_a_gt_b(a, b, res):
    assert (a > b) is res


def test_a_lt_or_eq_b():
    res = ["d", "o", "g"] <= ["d", "a", "y"]
    assert res is False


def test_identity_check():
    a = []
    b = a
    c = []
    assert all([
        a is b,
        a is not c,
        id(a) == id(b),
        id(a) != id(c),
        a == b,
        a == c
    ])


