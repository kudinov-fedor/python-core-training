from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    new_list = []
    find_border = bool
    for item in items:
        if item == border:
            find_border = True

    if find_border == True:
        border_position = items.index(border)
        while border_position < len(items):
            new_list.append(items[border_position])
            border_position += 1
        return new_list
    else:
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    # print("Coding complete? Click 'Check' to earn cool rewards!")
