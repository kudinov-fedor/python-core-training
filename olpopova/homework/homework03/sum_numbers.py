"""
*********************************************************************
Sum Numbers

In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
*********************************************************************
"""


def sum_numbers(text: str) -> int:
    words_list = text.split(" ")

    # final steps
    result_list = [int(i) for i in words_list if i.isdigit()]
    return sum(result_list)


def sum_numbers2(text: str) -> int:
    return sum((int(i) for i in text.split(" ") if i.isdigit()))
