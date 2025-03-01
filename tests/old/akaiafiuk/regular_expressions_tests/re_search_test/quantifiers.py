import re

import pytest


def test_exact_occurrence_number():
    """{n}: Matches exactly n occurrences of the preceding character or group."""
    match = re.search("(abc){2}d", "abcabcd")
    no_match = re.search("(abc){3}d", "abcabcd")
    assert match.group() == "abcabcd"
    assert no_match is None


def test_between_occurrence_number():
    """{n,m}: Matches between n and m (inclusive) occurrences of the preceding character or group."""
    pattern = "(abc){2,3}d"
    match = re.search(pattern, "abcabcd")
    also_match = re.search(pattern, "abcabcabcd")
    no_match = re.search(pattern, "abcd")
    assert match.group() == "abcabcd"
    assert also_match.group() == "abcabcabcd"
    assert no_match is None


def test_zero_or_more_occurrence():
    """* Matches zero or more occurrences of the preceding character or group."""
    pattern = "a*b"
    match = re.search(pattern, "b")
    also_match = re.search(pattern, "caaaab")
    assert match.group() == "b"
    assert also_match.group() == "aaaab"


def test_one_or_more_occurrence():
    """+ Matches zero or more occurrences of the preceding character or group."""
    pattern = "a+b"
    no_match = re.search(pattern, "b")
    match = re.search(pattern, "caaaab")
    assert no_match is None
    assert match.group() == "aaaab"


@pytest.mark.parametrize("search_string, result", [
    ("cb", "b"),
    ("cab", "ab"),
    ("aab", "ab")
])
def test_zero_or_one_occurrence(search_string, result):
    """? Matches zero or one occurrences of the preceding character or group."""
    pattern = "a?b"
    match = re.search(pattern, search_string)
    assert match.group() == result
