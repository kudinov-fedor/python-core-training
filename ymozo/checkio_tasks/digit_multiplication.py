def checkio(number: int) -> int:
    res = 1

    for num in str(number):
        if num != "0":
            res = res * int(num)

    return res


if __name__ == "__main__":
    print("Example:")
    print(checkio(123405))

    # These "asserts" are used for self-checking
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

    print("The mission is done! Click 'Check Solution' to earn rewards!")