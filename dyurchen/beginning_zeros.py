def beginning_zeros(number: str) -> int:
    result = 0
    for n in number:
        if int(n) == 0:
            result += 1
        else:
            break
    return result


