from typing import Iterable


def remove_all_before(items: list, border: int) -> list:
    items_list = list()
    if border in items:
        index_el = items.index(border)
        items_list = items[index_el:]
    else:
        items_list = items
    return items_list


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

