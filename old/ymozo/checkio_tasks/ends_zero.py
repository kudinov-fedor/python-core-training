def end_zeros(a: int) -> int:
    b = str(a)
    for index, num in enumerate(reversed(b)):
        if num != '0':
            break
    else:
        index = len(b)
    return index


def end_zeros_1(a: int) -> int:
    b = str(a)
    index = len(b) - len(b.rstrip("0"))
    return index


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(10))

    # These "asserts" are used for self-checking
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2

    assert end_zeros_1(0) == 1
    assert end_zeros_1(1) == 0
    assert end_zeros_1(10) == 1
    assert end_zeros_1(101) == 0
    assert end_zeros_1(245) == 0
    assert end_zeros_1(100100) == 2