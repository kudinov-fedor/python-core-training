"""
*********************************************************************
You should write a function that will receive a positive integer and return: "Fizz" if the number is divisible
by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").
*********************************************************************
"""


def checkio(num: int) -> str:
    return 'Fizz' if num % 3 == 0 else str(num)


"""
*********************************************************************
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.
*********************************************************************
"""


def checkio_complex(num: int) -> str:
    if num % 15 == 0:
        res = 'Fizz Buzz'
    elif num % 3 == 0:
        res = 'Fizz'
    elif num % 5 == 0:
        res = 'Buzz'
    else:
        res = str(num)
    return res
