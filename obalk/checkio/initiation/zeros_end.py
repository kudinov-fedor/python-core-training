def end_zeros(number: int) -> int:
    count = 0
    for number in str(number)[-1::-1]:
        if number == "0":
            count += 1
        else:
            break
    return count


def end_zeros_strip_len(number: int) -> int:
    value = str(number)
    return len(value) - len(value.rstrip('0'))
