import pytest
from anmykh.checkio import checkio_7


@pytest.mark.parametrize(["param", "result"], [
    [2, True],
    [5, False],
    [0, True]
])
def test_is_even(param, result):
    assert checkio_7.is_even(param) == result
