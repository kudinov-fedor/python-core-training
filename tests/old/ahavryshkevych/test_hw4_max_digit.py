import pytest
from ahavryshkevych.task_max_digit import max_digit


@pytest.mark.parametrize(["par1", "res"], [
    (0, 0),
    (52, 5),
    (634, 6),
    (1, 1),
    (10000, 1)
])
def test_max_digit(par1, res):
    assert max_digit(par1) == res
