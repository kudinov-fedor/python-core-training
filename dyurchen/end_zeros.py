def end_zeros(num: int) -> int:
    num_to_str = list(str(num))
    count_null = 0
    if num_to_str[-1] == '0':
        for elem in reversed(num_to_str):
            if int(elem) == 0:
                count_null += 1
            else:
                break
        return count_null
    return 0


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(1010))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
