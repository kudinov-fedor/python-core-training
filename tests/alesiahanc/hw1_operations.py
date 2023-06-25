import pytest


@pytest.mark.parametrize(["num1", "num2", "expected"], [
    (5, 2, 2),  # // shows only full numbers (quotient)
    (7, 2, 3)
])
def test_double_slash(num1, num2, expected):
    result = num1 // num2
    assert result == expected


@pytest.mark.parametrize(["num1", "num2", "expected"], [
    (5, 2, 1),  # % show only what is left (remainder)
    (7, 2, 1)
])
def test_percent(num1, num2, expected):
    result = num1 % num2
    assert result == expected


@pytest.mark.parametrize(["method", "num1", "num2", "expected"], [
    (divmod, 5, 2, (2, 1)),  # shows both quotient and remainder
    (divmod, 7, 2, (3, 1)),
    (pow, 5, 2, 25),  # power of number (5^2)
    (pow, 3, 2, 9)
])
def test_math_methods(method, num1, num2, expected):
    result = method(num1, num2)
    assert result == expected


@pytest.mark.parametrize(["arg1", "arg2", "expected"], [
    ("abc", "efg", "abcefg"),
    ((1, 2, 3), (4, 5, 6), (1, 2, 3, 4, 5, 6)),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])
])
def test_addition(arg1, arg2, expected):
    result = arg1 + arg2
    assert result == expected


@pytest.mark.parametrize(["arg1", "arg2", "expected"], [
    ("abc", 2, "abcabc"),
    (2, 5, 10),  # same result as if numbers were in ()
    ((1, 2, 3), 2, (1, 2, 3, 1, 2, 3)),
    ([1, 2, 3], 2, [1, 2, 3, 1, 2, 3]),
    ((2, ), 5, (2, 2, 2, 2, 2))
])
def test_multiplication(arg1, arg2, expected):
    result = arg1 * arg2
    assert result == expected
