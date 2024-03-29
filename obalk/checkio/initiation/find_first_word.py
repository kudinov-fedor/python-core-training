"""
You are given a string and you have to find its first word.

This is a simplified version of the First Word mission, which can be solved later.

The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
Input: A string.

Output: A string.

Example:

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"
"""


def first_word(sentence: str):
    return sentence.split(maxsplit=1)[0]
