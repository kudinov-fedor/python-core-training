import pytest

from yspryn.checkio_tasks.end_zero_hw5 import end_zeros, end_zeros2, end_zeros3, end_zeros4


@pytest.mark.parametrize("value, res", [
    (0, 1),
    (120093000, 3),
    (101, 0),
    (245, 0)
])
def test_end_zero(value, res):
    assert end_zeros(value) == res


@pytest.mark.parametrize("value, res", [
    (0, 1),
    (120093000, 3),
    (101, 0),
    (245, 0)
])
def test_end_zero2(value, res):
    assert end_zeros2(value) == res


@pytest.mark.parametrize("value, res", [
    (0, 1),
    (120093000, 3),
    (101, 0),
    (245, 0)
])
def test_end_zero3(value, res):
    assert end_zeros3(value) == res


@pytest.mark.parametrize("value, res", [
    (0, 1),
    (120093000, 3),
    (101, 0),
    (245, 0)
])
def test_end_zero4(value, res):
    assert end_zeros4(value) == res
