"""
You are given a string and you have to find its first word.

Input: A string.

Output: A string.
"""


def first_word(text: str) -> str:
    return str(text.split()[0]) if len(text) > 1 else text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
