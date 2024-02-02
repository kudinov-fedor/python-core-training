import pytest

from yspryn.checkio_tasks.end_zero_hw5 import end_zeros


@pytest.mark.parametrize("value, res", [
    (0, 1),
    (120093000, 3),
    (101, 0),
    (245, 0)
])
def test_end_zero(value, res):
    assert end_zeros(value) == res
