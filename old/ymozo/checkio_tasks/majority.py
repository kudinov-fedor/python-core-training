from typing import List


def is_majority(items: List[bool]) -> bool:

    true_count = sum(True for char in items if char)
    false_count = len(items) - true_count

    return true_count > false_count
