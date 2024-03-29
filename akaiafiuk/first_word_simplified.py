"""
You are given a string and you have to find its first word.
This is a simplified version of the First Word mission, which can be solved later.
The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.

Input: A string.
Output: A string.

Example:
first_word("Hello world") == "Hello"
"""


def first_word(text: str) -> str:
    if ' ' not in text:
        return text
    else:
        return text[0:text.index(' ')]


def first_word_using_split(text: str) -> str:
    text_list = text.split(' ')
    return text_list[0]
