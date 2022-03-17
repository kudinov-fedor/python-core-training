"""
You are given a string and you have to find its first word.
- The input string consists of only English letters and spaces.
- There aren’t any spaces at the beginning and the end of the string.
"""


def first_word(text: str) -> str:
    """
    returns the first word in a given text.
    """
    index_of_space = text.find(" ")
    if index_of_space < 0:
        index_of_space = len(text)
    return text[:index_of_space]
