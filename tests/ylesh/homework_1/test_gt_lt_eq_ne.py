import pytest


def test_equal():
    result = False == (3 * 0)
    assert result is True


def test_equal_id():
    a = []
    b = a
    result = True == (id(a) == id(b))
    assert result is True


@pytest.mark.parametrize(["param", "result"], [
    (1.5 <= (5 + 3) > len(["2", "e"]), True),
    ("a" in ["a", "b", "c"], True),
    (2 not in ("a", "b", "c"), True),
    (max([2, 3, 1, -2, -5, -8, 12]), 12),
    (min("banana", "ball", "cat", key=len), "cat")
])
def test_assertion(param, result):
    assert param is result
