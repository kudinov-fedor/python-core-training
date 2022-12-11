from typing import Any, List, Iterable


def replace_first(items: List[Any]) -> Iterable:
    if items:
        first_value = items.pop(0)
        items.append(first_value)
    return items


def replace_first_slice(items: list) -> list:
    return items[1:] + items[:1]
