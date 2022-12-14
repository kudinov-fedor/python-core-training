import pytest

from obalk.checkio.initiation.between_markers_simplified import between_markers


@pytest.mark.parametrize("text, start, end, result", [
    ("What is >apple<", ">", "<", "apple"),
    ("What is {apple}", "{", "}", "apple"),
    ("What is [an apple]", "[", "]", "an apple"),
    ("What is ><", ">", "<", ""),
])
def test_end_zeros(text, start, end, result):
    assert between_markers(text, start, end) == result
