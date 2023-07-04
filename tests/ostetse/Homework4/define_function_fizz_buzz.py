def checkio(num: int) -> str:
    """
    You should write a function that will receive a positive integer and return:
    "Fizz Buzz" if the number is divisible by 3 and by 5;
    "Fizz" if the number is divisible by 3;
    "Buzz" if the number is divisible by 5;
    The number as a string for other cases.
    Input: An integer (int).
    Output: A string (str).
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)
