"""
**********************************************************************
Three Words

Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters.
You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end"
contains three words in succession.
**********************************************************************
"""
import pytest


def checkio(words: str) -> bool:

    # edge cases
    words_list = words.split()
    list_size = len(words_list)
    if list_size < 3:
        return False

    # final steps
    for i in range(0, list_size - 1):
        if i <= list_size - 3:

            is_all_alpha = all(map(str.isalpha, words_list[i: i + 3]))

            if not is_all_alpha:
                continue

        return is_all_alpha


@pytest.mark.parametrize(['words', 'expected'], [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 bla 3 4", False),
    ("bla 1 bla bla bla", True),
    ("Hi", False),
    ('one two 3 four five 6 seven eight 9 ten eleven 12', False)
])
def test_checkio(words, expected):
    assert checkio(words) is expected
