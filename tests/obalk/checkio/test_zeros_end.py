import pytest
from obalk.checkio.zeros_end import end_zeros, end_zeros_strip_len


@pytest.mark.parametrize("function", [end_zeros, end_zeros_strip_len])
@pytest.mark.parametrize("number, result", [
    (111, 0),
    (0, 1),
    (101, 0),
    (100, 2),
    (100100, 2),
])
def test_end_zeros(function, number, result):
    assert function(number) == result
