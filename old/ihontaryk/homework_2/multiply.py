from numbers import Number


def multiply_numbers(number1, number2):
    """
    multiply_numbers function
    """
    both_numbers = isinstance(number1, Number) and isinstance(number2, Number)
    if not both_numbers:
        raise TypeError(f"You used wrong type: expected int or float for both arguments")

    return number1 * number2
