def beginning_zeros(a: str) -> int:
    for index, num in enumerate(a):
        if num != '0':
            break
    else:
        index = len(a)
    return index


if __name__ == "__main__":
    print("Example:")
    print(beginning_zeros("10"))

    # These "asserts" are used for self-checking
    assert beginning_zeros("100") == 0
    assert beginning_zeros("001") == 2
    assert beginning_zeros("100100") == 0
    assert beginning_zeros("001001") == 2
    assert beginning_zeros("012345679") == 1
    assert beginning_zeros("0000") == 4

    print("The mission is done! Click 'Check Solution' to earn rewards!")