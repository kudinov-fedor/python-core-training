from typing import List


def is_majority(items: List[bool]) -> bool:

    true_count = sum(1 for char in items if char)
    false_count = len(items) - true_count

    return true_count > false_count


if __name__ == "__main__":
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")
