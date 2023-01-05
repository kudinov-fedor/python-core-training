"""
You are given a string and you have to find its first word.

Input: A string.

Output: A string.

Example:

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi
"""
def first_word(text: str) -> str:
    # your code here
    return text.split()[0]

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"