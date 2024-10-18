def min(*args, key=None):
    min_item = args[0]
    for item in args:
        if key:
            min_item = item if key(item) < key(min_item) else min_item
        else:
            min_item = item if item < min_item else min_item
    return min_item


def max(*args, key=None):
    max_item = args[0]
    for item in args:
        if key:
            max_item = item if key(item) > key(max_item) else max_item
        else:
            max_item = item if item > max_item else max_item
    return max_item


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    items = [*args]
    sorted_list = []
    while len(items) > 0:
        item = max(*items, key=key) if reverse else min(*items, key=key)
        sorted_list.append(item)
        items.remove(item)
    return sorted_list
