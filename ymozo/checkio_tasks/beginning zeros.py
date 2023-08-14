def beginning_zeros(a: str) -> int:
    converted_a = list(a)
    zero_count = 0
    for num in converted_a:
        if int(num) == 0:
            zero_count += 1
        else:
            break
    return zero_count


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