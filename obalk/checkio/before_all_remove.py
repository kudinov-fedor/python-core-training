from typing import Any, List, Iterable


def remove_all_before(items: List[Any], border: int) -> Iterable:
    try:
        return items[items.index(border):]
    except ValueError:
        return items


def remove_all_before_boolean(items: List[Any], border: int) -> Iterable:
    return border in items and items[items.index(border):] or items
