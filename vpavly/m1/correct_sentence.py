"""
For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string.

Output: A string.
"""


def correct_sentence(sentence: str) -> str:
    try:
        first_char = sentence[0].upper() if not sentence[0].isupper() else sentence[0]
        last_char = sentence[-1] + '.' if not sentence[-1].endswith('.') else sentence[-1]
        return first_char + sentence[1:-1] + last_char
    except IndexError:
        return ''
