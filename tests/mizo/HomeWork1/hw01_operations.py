import pytest


@pytest.mark.parametrize(["num1", "num2", "res"], [
    (10, 2, 5),
    (8, 2, 4)
])
def test_divide_numbers(num1, num2, res):
    result = num1 / num2
    assert result == res


# operations on sequences
@pytest.mark.parametrize("expected", [
    ([1, 2, 1, 2, 1, 2])
])
def test_multiply_sequence(expected):
    result = [1, 2] * 3  # the result will be [1,2,1,2,1,2]
    assert result == expected
