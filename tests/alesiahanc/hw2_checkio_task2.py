"""
In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.
"""


def sum_numbers(text: str) -> int:
    elements = text.split(" ")
    return sum(int(x) for x in elements if x.isdigit())


if __name__ == '__main__':
    sum_numbers("who is 1st here")
