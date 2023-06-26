def is_even(num: int) -> bool:
    return num % 2 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")