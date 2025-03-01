from typing import List


def checkio(array: List[int]) -> int:
    return sum(array[::2]) * array[-1] if len(array) else 0
