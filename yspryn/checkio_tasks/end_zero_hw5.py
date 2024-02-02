# Try to find out how many zeros a given number has at the end.


def end_zeros(a: int) -> int:
    res = 0
    for i in reversed(str(a)):
        if i == "0":
            res += 1
        else:
            break
    return res
