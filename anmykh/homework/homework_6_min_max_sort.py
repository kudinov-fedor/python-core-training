def max_function(*items, key=lambda i: i):
    if len(items) == 1:
        items = items[0]
    if len(items) == 0:
        raise ValueError
    max_value = items[0]
    for item in items[1:]:
        if key(item) > key(max_value):
            max_value = item
    return max_value


def min_function(*items, key=lambda i: i):
    if len(items) == 1:
        items = items[0]
    if len(items) == 0:
        raise ValueError
    min_value = items[0]
    for item in items[1:]:
        if key(item) < key(min_value):
            min_value = item
    return min_value


def sort_function(*items, key=lambda i: i, reverse=False):
    if not items:
        return []
    if len(items) == 1:
        items = list(items[0])
    sorted_list = []
    func = max if reverse else min
    items_list = list(items)
    while items_list:
        item = func(items_list, key=key)
        items_list.remove(item)
        sorted_list.append(item)
    return sorted_list
