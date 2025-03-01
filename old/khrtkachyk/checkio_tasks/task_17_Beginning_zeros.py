"""
You have a string that consist only of digits. You need to find how many zero
digits ("0") are at the beginning of the given string.

Input: A string (str), that consists of digits.
Output: An integer (int).
"""


def beginning_zeros(a: str) -> int:
    for i, val in enumerate(a):
        if val != "0":
            return i
    return len(a)


def beginning_zeros2(a: str) -> int:
    cut_by_zeros = a.lstrip("0")
    return len(a) - len(cut_by_zeros)


def beginning_zeros3(a:str) -> int:
    if a.startswith("0"):
        return 1 + beginning_zeros(a[1:])
    else:
        return 0


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros("10"))
    print(beginning_zeros("100"))
    print(beginning_zeros("001"))
    print(beginning_zeros("100100"))
    print(beginning_zeros("001001"))

    print(beginning_zeros2("100100"))
    print(beginning_zeros2("001001"))
    print(beginning_zeros2("10"))
    print(beginning_zeros2("100"))
    print(beginning_zeros2("001"))

    print(beginning_zeros3("100100"))
    print(beginning_zeros3("001001"))
    print(beginning_zeros3("10"))
    print(beginning_zeros3("100"))
    print(beginning_zeros3("001"))
