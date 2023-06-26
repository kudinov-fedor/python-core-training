"""
***** Task5 *********************************************************
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
*********************************************************************
"""


def checkio(num: int) -> str:
    if num % 15 == 0:
        res = 'Fizz Buzz'
    elif num % 3 == 0:
        res = 'Fizz'
    elif num % 5 == 0:
        res = 'Buzz'
    else:
        res = str(num)
    return res


# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"
