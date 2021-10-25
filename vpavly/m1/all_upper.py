"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.
"""


# def is_all_upper(text: str) -> bool:
#     return text.isupper()


def is_all_upper(text: str) -> bool:
    big_letters = [32] + list(range(65, 91)) + list(range(48, 58))
    for letter in text:
        if ord(letter) not in big_letters:
            return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL uPPER'))
