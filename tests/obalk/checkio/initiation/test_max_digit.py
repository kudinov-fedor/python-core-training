import pytest

from obalk.checkio.initiation.max_digit import max_digit, max_digit_div


@pytest.mark.parametrize("function", [
    max_digit,
    max_digit_div
])
@pytest.mark.parametrize("number, result", [
    (0, 0),
    (123, 3),
    (980, 9)
])
def test_max_digit(function, number, result):
    assert function(number) == result
