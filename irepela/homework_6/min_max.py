def min(*args, key=None):
    items = list(*args)
    min_item = items[0]
    for item in items:
        if key:
            min_item = item if key(item) < key(min_item) else min_item
        else:
            min_item = item if item < min_item else min_item
    return min_item


def max(*args, key=None):
    items = list(*args)
    max_item = items[0]
    for item in items:
        if key:
            max_item = item if key(item) > key(max_item) else max_item
        else:
            max_item = item if item > max_item else max_item
    return max_item


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    items = list(*args)
    sorted_list = []
    while len(items) > 0:
        item = max(items, key=key) if reverse else min(items, key=key)
        sorted_list.append(item)
        items.remove(item)
    return sorted_list
