"""
You should write a function that will receive a positive integer and return:

- "Fizz Buzz" if the number is divisible by 3 and by 5;
- "Fizz" if the number is divisible by 3;
- "Buzz" if the number is divisible by 5;
- The number as a string for other cases.

Input: An integer (int).
Output: A string (str).
"""


def checkio(num: int) -> str:
    if num % 5 == 0 and num % 3 == 0:
        return "Fizz Buzz"
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


if __name__ == '__main__':
    print("Example:")
    print(checkio(30))
    print(checkio(6))
    print(checkio(10))
    print(checkio(7))
