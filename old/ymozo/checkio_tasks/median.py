from __future__ import annotations
from typing import List


def checkio(data: List[int]) -> int | float:
    sorted_list = sorted(data)
    lst = len(sorted_list)

    if lst % 2 != 0:
        middle_index = lst // 2
        return sorted_list[middle_index]

    first_mid_index = lst // 2 - 1
    second_mid_index = lst // 2
    return (sorted_list[first_mid_index] + sorted_list[second_mid_index]) / 2


if __name__ == "__main__":
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking
    assert checkio([1, 2, 3, 4, 5]) == 3
    assert checkio([3, 1, 2, 5, 3]) == 3
    assert checkio([1, 300, 2, 200, 1]) == 2
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
    assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
    assert checkio([33, 56, 62]) == 56
    assert checkio([21, 56, 84, 82, 52, 9]) == 54
    assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
    assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

    print("The mission is done! Click 'Check Solution' to earn rewards!")

