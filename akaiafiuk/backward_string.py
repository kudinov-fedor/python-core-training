"""
You should return a given string in reverse order.
Input: A string.
Output: A string.
"""


def backward_string(val: str) -> str:
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))
