"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it -
function should return True.
Input: A string.
Output: a boolean.
"""


def is_all_upper(text: str) -> bool:
    trimmed_table = text.maketrans('1234567890 ', "           ")
    trimmed_string = text.translate(trimmed_table)
    if trimmed_string.strip() == '':
        return True
    else:
        return trimmed_string.isupper()


def is_all_upper_v2(text: str) -> bool:
    trimmed_string = ''.join([i for i in text if i.isalpha()])
    if not trimmed_string:
        return True
    else:
        return trimmed_string.isupper()


def is_all_upper_v3(text: str) -> bool:
    return not bool([i for i in text if i.islower() and i.isalpha()])


def is_all_upper_v4(text: str) -> bool:
    return text == text.upper()
