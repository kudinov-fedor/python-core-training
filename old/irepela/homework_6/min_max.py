def min(*args, key=lambda i: i):
    min_item = args[0]

    for item in args:
        min_item = item if key(item) < key(min_item) else min_item

    return min_item


def max(*args, key=lambda i: i):
    max_item = args[0]

    for item in args:
        max_item = item if key(item) > key(max_item) else max_item

    return max_item


def sorted(*args, key=lambda i: i, reverse=False):
    """Ascending by default"""
    items = [*args]
    sorted_list = []

    func = max if reverse else min
    while len(items) > 0:
        item = func(*items, key=key)
        sorted_list.append(item)
        items.remove(item)

    return sorted_list
