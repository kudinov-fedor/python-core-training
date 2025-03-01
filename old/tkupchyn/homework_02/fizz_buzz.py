def fizz_buzz(n: int) -> str:
    """
    Returns 'Fizz', 'Buzz', or 'FizzBuzz' based on divisibility of the input integer `n`.

    Args:
    n (int): The input integer to be evaluated.

    Returns:
    str: 'Fizz', 'Buzz', 'FizzBuzz', or the input number as a string.
    """
    if n % 15 == 0:
        result = "FizzBuzz"
    elif n % 3 == 0:
        result = "Fizz"
    elif n % 5 == 0:
        result = "Buzz"
    else:
        result = str(n)

    return result
