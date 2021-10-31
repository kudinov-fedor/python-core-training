from typing import Iterable


def remove_all_before(items: list, border: int) -> list:
    items_list = list()
    for i in range(len(items)):
        if items[i] == border:
            items_list = items[i:]
        else:
            items_list = items
    return items_list


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([], 0)))

