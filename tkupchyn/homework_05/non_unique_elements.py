from collections import Counter
from typing import Generator


def remove_unique_values(iterable: list) -> Generator:
    """
    Removes unique values from a list and returns an iterable with only non-unique values.

    Args:
        iterable (list): a non-empty sequence of integers.
    Returns:
        Iterable: Iterable consisting of only the non-unique elements from the initial sequence
    """
    counts = Counter(iterable)
    return (elem for elem in iterable if counts[elem] > 1)


def remove_unique_values_alternative(iterable: list) -> Generator:
    return (elem for elem in iterable if iterable.count(elem) > 1)
