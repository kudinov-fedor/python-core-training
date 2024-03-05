import pytest
from anmykh.checkio.checkio_7 import is_even


@pytest.mark.parametrize(["param", "result"], [
    [2, True],
    [5, False],
    [0, True]
])
def test_is_even(param, result):
    assert is_even(param) == result
