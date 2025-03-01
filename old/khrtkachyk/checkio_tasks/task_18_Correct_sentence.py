"""
For the input of your function, you will be given one sentence.
You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all the fixes are necessary.
If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string (str).
Output: A string (str).

Precondition: No leading and trailing spaces, text contains only spaces, a-z, A-Z, "," and ".".
"""


def correct_sentence(text: str) -> str:
    res = text[0].capitalize() + text[1:]
    if not res.endswith("."):
        res += "."
    return res


def correct_sentence_2_0(text: str) -> str:
    return text[0].capitalize() + text[1:].rstrip(".") + "."
