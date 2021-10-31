"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.
"""


def is_all_upper(text: str) -> bool:
    return text.upper() == text


# def is_all_upper(text: str) -> bool:
#     big_letters = [32] + list(range(65, 91)) + list(range(48, 58))
#     return all(ord(letter) in big_letters for letter in text)
#
