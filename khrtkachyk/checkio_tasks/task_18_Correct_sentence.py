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
    res = text.endswith(".")
    res1 = text[0].istitle()
    if res and res1:
        return text
    elif res and not res1:
        return f"{text[0].upper() + text[1:]}"
    else:
        return f"{text[0].upper() + text[1:]}."


def correct_sentence_2_0(text: str) -> str:
    return text[0].capitalize() + text[1:].rstrip(".") + "."
