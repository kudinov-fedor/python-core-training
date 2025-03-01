import pytest

from obalk.checkio.initiation.beginning_zeros import beginning_zeros


@pytest.mark.parametrize("number, result", [
    ("111", 0),
    ("0", 1),
    ("101", 0),
    ("001", 2),
    ("100100", 0),
])
def test_end_zeros(number, result):
    assert beginning_zeros(number) == result
