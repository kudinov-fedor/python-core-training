def checkio(num: int) -> str:
    """
    You should write a function that will receive a positive integer and return:
    - "Fizz" if the number is divisible by 3 (3, 6, 9 ...)
    otherwise convert the given number to a string (2 -> "2")
    Input: An integer (int).
    Output: A string (str).
    """
    if num % 3 == 0:
        return "Fizz"
    else:
        return str(num)
