"""
I might see a simplified version of this mission already First Word (simplified) . This mission is a little bit more complex as not only English letters can be in the given string.

You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, one/multiple dot(s) or space(s).
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.

Example:

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
1
2
3
4
How it is used: the first word is a command in a command line
"""
import re


def first_word(text: str) -> str:
    pattern = r"[a-zA-Z\']+"
    words = re.findall(pattern, text)
    return words[0] if words else ""
