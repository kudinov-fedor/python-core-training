import pytest
from tkupchyn.homework_05.popular_words import popular_words

text_1 = "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n"
text_2 = ("At the input of your function are given 2 arguments: the text and the array of words the popularity of "
          "which you need to determine.")


@pytest.mark.parametrize("text, words_to_find, expected_result",
                         [
                             (text_1, ["i", "was", "three", "near"],  {"i": 4, "was": 3, "three": 0, "near": 0}),
                             (text_2, ["the", "of", "attention"], {"the": 4, "of": 3, "attention": 0})
                         ])
def test_popular_words(text, words_to_find, expected_result):
    assert popular_words(text, words_to_find) == expected_result
