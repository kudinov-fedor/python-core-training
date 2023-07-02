"""
For the input of your function, you will be given one sentence.
You have to return a corrected version,
that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary.
If a sentence already ends with a period (dot),
then adding another one will be a mistake.
"""


def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]  # change first element to uppercase
    if text[-1] != ".":  # check of the last element is not a period
        text = text + "."
    return text
