"""
You have a non-negative integer. Try to find out how many digits it has.

Input: A non-negative integer (int).
Output: An integer (int)
"""


def number_length(value: int) -> int:
    return len(str(value))


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))
    print(number_length(0))
    print(number_length(4444))
