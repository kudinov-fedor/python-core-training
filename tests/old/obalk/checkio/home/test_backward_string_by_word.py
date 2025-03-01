import pytest

from obalk.checkio.home.backward_each_word import backward_string_by_word, backward_string_by_word_reverse


@pytest.mark.parametrize("function", [
    backward_string_by_word,
    backward_string_by_word_reverse
])
@pytest.mark.parametrize("text, result", [
    ("", ""),
    ("world", "dlrow"),
    ("hello   world", "olleh   dlrow"),
    ("olleH Hello", "Hello olleH")
])
def test_duplicate_zeros(function, text, result):
    assert function(text) == result
