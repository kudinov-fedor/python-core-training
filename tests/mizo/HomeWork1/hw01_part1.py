import pytest


@pytest.mark.parametrize(["par1", "par2", "res"], [
    ("z", ["a", "b", "c"], True),
    ("z", "abc", True),
    ("z", ("a", "b", "c"), True)
])
def check_contains_in(par1, par2, res):
    result = par1 not in par2
    assert result is res


# double comparison
@pytest.mark.parametrize(["num1", "num2", "num3", "res"], [
    (1, 5, 9, True)
])
def test_double_comparison(num1, num2, num3, res):
    result = num1 <= num2 <= num3
    assert result == res


# same as
a = 10
b = 15


@pytest.mark.parametrize(["arg1", "arg2", "expected"], [
    [id(a), id(b), False]
])
def test_same_as(arg1, arg2, expected):
    result = arg1 == arg2
    assert result is expected


# implicit comparison

@pytest.mark.parametrize("param1, res", [
    ([2, 3, 1, -2, -5, -8, 12], 12)
])
def test_implicit_comparison(param1, res):
    result = max(param1, key=lambda x: abs(x))  # abs absolute value
    assert result == res


# implicit comparison2
@pytest.mark.parametrize("param1, param2, param3, key, res", [
    ("banana", "ball", "cat", len, "banana")
])
def test_implicit_comparison2(param1, param2, param3, key, res):
    result = max(param1, param2, param3, key=key)
    assert result == res
