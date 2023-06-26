"""
You should write a function that will receive a positive integer and return: "Fizz"
if the number is divisible by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").

Input: An integer (int).
Output: A string (str).
"""


def just_fizz(num: int) -> str:
    return "Fizz" if (num % 3 == 0) else str(num)


if __name__ == '__main__':
    print("Example:")
    print(just_fizz(2))
    print(just_fizz(6))
