"""
****** Task3 ********************************************************
Sum Numbers

In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
*********************************************************************
"""
import pytest


@pytest.mark.parametrize(['text', 'expected'], [
    ("hi", 0),
    ("who is 1st here", 0),
    ("my numbers is 2", 2),
    ("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year", 3755),
    ("5 plus 6 is", 11),
    ("", 0)
])
def sum_numbers(text, expected):
    result_list = []

    # edge cases
    words_list = text.split(" ")
    if len(words_list) == 1 and not words_list[0].isdigit():
        return sum(result_list)

    # final steps
    for i in words_list:
        if i.isdigit():
            result_list.append(int(i))

    assert sum(result_list) == expected
