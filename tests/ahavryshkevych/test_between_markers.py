import pytest

from ahavryshkevych.task_between_markers import between_markers


@pytest.mark.parametrize(["par1", "par2", "par3", "res"], [
    ("What is >apple<", ">", "<", "apple"),
    ("What is [apple]", "[", "]", "apple"),
    ("What is ><", ">", "<", ""),
    ("[an apple]", "[", "]", "an apple")
])
def test_between_markers(par1, par2, par3, res):
    assert between_markers(par1, par2, par3) == res