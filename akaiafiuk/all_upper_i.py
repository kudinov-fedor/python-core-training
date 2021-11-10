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
