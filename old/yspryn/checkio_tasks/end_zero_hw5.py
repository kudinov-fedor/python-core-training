# Try to find out how many zeros a given number has at the end.


def end_zeros(a: int) -> int:
    res = 0
    for i in reversed(str(a)):
        if i == "0":
            res += 1
        else:
            break
    return res


def end_zeros2(a: int) -> int:
    res = 0
    for i in reversed(str(a)):
        if i != "0":
            break
        res += 1
    return res


def end_zeros3(a: int) -> int:
    b = str(a).rstrip('0')
    return len(str(a)) - len(b)


def end_zeros4(a: int) -> int:
    for counter, i in enumerate(reversed(str(a)), start=1):
        print(counter, i)
        if i != '0':
            if counter:
                counter = counter - 1
            break
    return counter
