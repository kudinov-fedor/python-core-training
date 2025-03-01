"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.
"""


def backward_string_by_word(text: str) -> str:
    return " ".join([word[::-1] for word in text.split(" ")])


def backward_string_by_word_reverse(text: str) -> str:
    split_text = text.split(' ')
    reversed_text = ' '.join(reversed(split_text))
    return reversed_text[::-1]
