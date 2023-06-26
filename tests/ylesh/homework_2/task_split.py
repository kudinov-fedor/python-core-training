"""
You are given a string and you have to find its first word.
"""


def first_word(text: str) -> str:
    return text.split()[0]


print(first_word("Hello world!"))
