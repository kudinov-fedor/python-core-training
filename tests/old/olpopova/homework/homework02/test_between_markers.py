import pytest

from olpopova.homework.homework02.between_markers import between_markers


@pytest.mark.parametrize(['text', 'start', 'end', 'expected'], [
    ("What is >apple<", ">", "<", "apple"),
    ("What is [apple]", "[", "]", "apple"),
    ("What is ><", ">", "<", ""),
    ("[an apple]", "[", "]", "an apple")
    ])
def test_between_markers(text, start, end, expected):
    assert between_markers(text, start, end) == expected
