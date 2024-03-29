import pytest
from ahavryshkevych.task_goes_right_after import goes_after, goes_after2, goes_after3


@pytest.mark.parametrize(["par1", "par2", "par3", "res"], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False),
    ("camel", "b", "f", False),
    ("partial", "a", "l", True),
])
def test_char_sequence(par1, par2, par3, res):
    assert goes_after(par1, par2, par3) == res


@pytest.mark.parametrize(["par1", "par2", "par3", "res"], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False),
    ("camel", "b", "f", False),
    ("partial", "a", "l", True),
])
def test_goes_after2(par1, par2, par3, res):
    assert goes_after2(par1, par2, par3) == res


@pytest.mark.parametrize(["par1", "par2", "par3", "res"], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False),
    ("camel", "b", "f", False),
    ("partial", "a", "l", True),
])
def test_goes_after3(par1, par2, par3, res):
    assert goes_after3(par1, par2, par3) == res
