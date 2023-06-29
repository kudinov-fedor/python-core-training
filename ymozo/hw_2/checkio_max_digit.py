def max_digit(value: int) -> int:
    str_num = str(value)
    max_val = 0
    for digit in str_num:
        if digit.isdigit():
            current_num = int(digit)
            if current_num > max_val:
                max_val = current_num

    return max_val


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
