def max_digit(value: int) -> int:
    str_num = str(value)
    tuple_of_numbers = tuple(int(char) for char in str_num)
    max_value = max(tuple_of_numbers)
    return max_value


if __name__ == '__main__':
    print("Example:")
    print(max_digit(10))

    # These "asserts" are used for self-checking
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1

    print("The mission is done! Click 'Check Solution' to earn rewards!")
