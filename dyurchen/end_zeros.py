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

