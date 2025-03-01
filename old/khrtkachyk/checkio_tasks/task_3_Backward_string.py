"""
You should return a given string in reverse order.

Input: A string (str).
Output: A string (str).
"""


def backward_string(val: str) -> str:
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string("val"))
    print(backward_string(""))
    print(backward_string("ohho"))
    print(backward_string("123456789"))
