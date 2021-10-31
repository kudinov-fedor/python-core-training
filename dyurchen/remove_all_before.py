from typing import Iterable


def remove_all_before(items: list, border: int) -> list:
    for i in range(0, len(items)):
        if items[i] == border:
            return items[i:]
    return items


