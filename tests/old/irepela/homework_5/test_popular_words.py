import pytest
from irepela.homework_5.popular_words import popular_words


@pytest.mark.parametrize("a, b, expected", [
    ("\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
     ["i", "was", "three", "near"], {"i": 4, "was": 3, "three": 0, "near": 0}),
    ("It's flying from somewhere\nAs fast as it can\nI couldn't keep up with it\nNot if I ran",
     ["it's", 'ran', 'i'], {"it's": 1, "ran": 1, "i": 2}),

])
def test_popular_words(a, b, expected):
    assert popular_words(a, b) == expected
