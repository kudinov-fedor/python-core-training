from math import log10


def number_length(value: int) -> int:
    return len(str(value))


def number_length_math(value: int) -> int:
    return int(log10(max(1, value))) + 1
