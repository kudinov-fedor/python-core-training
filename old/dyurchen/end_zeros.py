def end_zeros(num: int) -> int:
    num_to_str = str(num)
    count_null = 0
    for i in num_to_str[::-1]:
        if i == '0':
            count_null += 1
        else:
            break
    return count_null
