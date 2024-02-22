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


if __name__ == "__main__":
    assert reduce_function(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce_function(key=mul, default=1) == 1
    assert reduce_function(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce_function(key=add, default=0) == 0
    assert sum_function(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8
