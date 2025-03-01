"""
In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.

Input: A string (str).
Output: An integer (int).
"""


def sum_numbers(text: str) -> int:
    new_list = text.split()
    res = [int(item) for item in new_list if item.isnumeric()]
    print(res)
    summarized = sum(res)
    return summarized


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers("hi 15 there 0"))
