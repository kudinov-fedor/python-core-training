import pytest
from ahavryshkevych.task_goes_right_after import goes_after


@pytest.mark.parametrize(["par1", "par2", "par3", "res"], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False)
])
def test_char_sequence(par1, par2, par3, res):
    assert goes_after(par1, par2, par3) == res
