import pytest

from ahavryshkevych.task_beginning_zeros import beginning_zeros


@pytest.mark.parametrize(["arg", "res"], [
    ("100", 0),
    ("001", 2),
    ("100100", 0),
    ("001001", 2),
    ("012345679", 1),
    ("0000", 4)
])
def test_beginning_zeros(arg, res):
    assert beginning_zeros(arg) == res
