def checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


if __name__ == '__main__':
    print("Example:")
    print(checkio(3))

    # These "asserts" are used for self-checking
    assert checkio(15) == "Fizz"
    assert checkio(6) == "Fizz"
    assert checkio(10) == "10"
    assert checkio(7) == "7"

    print("The mission is done! Click 'Check Solution' to earn rewards!")