import pytest

from vpavly.additional.decorator import gen_random


@pytest.mark.parametrize('expected', [0.5])
def test_gen_random(expected):
    try:
        res = gen_random()  # raises error or return float < 0.5
    except AssertionError:
        res = 0  # any default just so that test would not fail
    assert res < 0.5
