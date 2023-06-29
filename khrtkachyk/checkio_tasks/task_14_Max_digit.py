"""
You have a number, and you need to determine which digit in this number is the biggest.

Input: A positive integer (int).
Output: An integer 0-9 (int).
"""


def max_digit(value: int) -> int:
    converted_to_list = [int(i) for i in str(value)]
    return max(converted_to_list)


if __name__ == '__main__':
    print("Example:")
    print(max_digit(10))
