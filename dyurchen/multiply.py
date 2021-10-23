def mult_two(a: int, b: int) -> int:
    mult = a * b
    return mult


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0