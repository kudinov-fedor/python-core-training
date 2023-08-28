import functools


def checkio(number: int) -> int:
    res = 1

    for num in str(number).replace("0", ""):
        res = res * int(num)

    return res


def checkio_1(number: int) -> int:
    digits = (int(digit) for digit in str(number) if digit != '0')
    result = functools.reduce(lambda a, b: a*b, digits, 1)

    return result


if __name__ == "__main__":
    print("Example:")
    print(checkio(123405))

    # These "asserts" are used for self-checking
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

    assert checkio_1(123405) == 120
    assert checkio_1(999) == 729
    assert checkio_1(1000) == 1
    assert checkio_1(1111) == 1
    assert checkio_1(0000) == 1
    print("The mission is done! Click 'Check Solution' to earn rewards!")