def fizz_buzz(number: int) -> str:
    """
        Checks if number is divisible by certain numbers
        and returns proper string depending on that

        Args:
            number (int): input number

        Returns:
            str: "Fizz Buzz" if number is divisible by 3 and 5
                 "Fizz" if number is divisible by 3
                 "Buzz" if number is divisible by 5
                 string representation of a number in other cases
    """
    result = str(number)

    if number % 15 == 0:
        result = "Fizz Buzz"
    elif number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result = "Buzz"

    return result
