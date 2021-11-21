"""
In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

Input: A string.

Output: An int.
"""


def sum_numbers(text: str) -> int:
    result = 0
    for word in text.split():
        if word.isdigit():
            result += int(word)
    return result


sum_numbers_lambda = lambda text: sum(int(word) for word in text.split() if word.isdigit())
