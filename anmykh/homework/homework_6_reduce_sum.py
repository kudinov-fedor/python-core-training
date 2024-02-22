from operator import add, mul


def reduce_function(*items, key: callable, default):
    if len(items) == 0:
        return default
    result, *items = items
    for item in items:
        result = key(result, item)
    return result


def sum_function(*items):
    return reduce_function(*items, key=add, default=0)
