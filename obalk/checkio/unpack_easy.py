from typing import Tuple


def easy_unpack(elements: Tuple[int, ...]) -> Tuple[int, int, int]:
    return elements[0], elements[2], elements[-2]
