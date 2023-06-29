"""
****** Task3 ********************************************************
Sum Numbers

In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
*********************************************************************
"""
import pytest


def sum_numbers(text: str) -> int:
    words_list = text.split(" ")

    # final steps
    result_list = [int(i) for i in words_list if i.isdigit()]
    return sum(result_list)


def sum_numbers2(text: str) -> int:
    return sum((int(i) for i in text.split(" ") if i.isdigit()))


@pytest.mark.parametrize(['text', 'expected'], [
    ("hi", 0),
    ("who is 1st here", 0),
    ("my numbers is 2", 2),
    ("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year", 3755),
    ("5 plus 6 is", 11),
    ("", 0)
])
def test_sum_numbers(text, expected):
    assert sum_numbers(text) == expected
    assert sum_numbers2(text) == expected
