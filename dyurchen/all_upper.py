from typing import Iterable


def replace_first(items: list) -> list:
    if len(items) != 0:
        first_elem = items.pop(0)
        items.append(first_elem)
    return items
