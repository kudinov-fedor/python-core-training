import pytest

from obalk.checkio.initiation.split_pairs import split_pairs, split_pairs_zip, split_pairs_iter_tools


@pytest.mark.parametrize("function", [
    split_pairs,
    split_pairs_zip,
    split_pairs_iter_tools
])
@pytest.mark.parametrize("text, result", [
    ("abcd", ["ab", "cd"]),
    ("abcdf", ["ab", "cd", "f_"]),
    ("a", ["a_"]),
    ([], [])
])
def test_max_digit(function, text, result):
    assert function(text) == result
