def max_digit(number: int) -> int:
    list_of_numbers = list(str(number))
    max_number = max(list_of_numbers)
    return int(max_number)
