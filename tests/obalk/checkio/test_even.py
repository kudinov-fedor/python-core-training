import pytest
from obalk.checkio.even import is_even


@pytest.mark.parametrize("number, result", [
    (2, True),
    (5, False),
    (0, True)
])
def test_is_even(number, result):
    assert is_even(number) == result
