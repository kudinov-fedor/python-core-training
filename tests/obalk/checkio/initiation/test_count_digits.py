import pytest

from obalk.checkio.initiation.count_digits import count_digits, count_digits_regex


@pytest.mark.parametrize("function", [
    count_digits,
    count_digits_regex
])
@pytest.mark.parametrize("number, result", [
    ("I am 18", 2),
    ("There is no digit here", 0),
    ("", 0),
    ("2 + 2 = 4", 3),
])
def test_end_zeros(function, number, result):
    assert function(number) == result
