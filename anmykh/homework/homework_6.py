def max_function(*items, key=None):
    if len(items) == 0:
        return ValueError
    if len(items) == 1:
        items = tuple(items[0])
    if len(items) == 0:
        return ValueError
    max_value = items[0]
    for item in items[1:]:
        if item > max_value:
            max_value = item
    return max_value


def min_function(*items, key=None):
    if len(items) == 0:
        return ValueError
    if len(items) == 1:
        items = tuple(items[0])
    if len(items) == 0:
        return ValueError
    min_value = items[0]
    for item in items[1:]:
        if item < min_value:
            min_value = item
    return min_value


def sort_function(items):
    length = len(items)
    if length == 0:
        return []
    if type(items) is not list:
        items = list(items)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
