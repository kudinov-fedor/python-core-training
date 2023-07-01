"""
You have a string that consist only of digits. You need to find how many zero
digits ("0") are at the beginning of the given string.

Input: A string (str), that consists of digits.
Output: An integer (int).
"""


def beginning_zeros(a: str) -> int:
    first = 0
    for i in a:
        if a[0] == i == "0":
            first += 1
            continue
        else:
            return first
    return first


def beginning_zeros2(a: str) -> int:
    cut_by_zeros = a.lstrip("0")
    return len(a) - len(cut_by_zeros)


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
