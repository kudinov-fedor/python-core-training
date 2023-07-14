from operator import add, mul


def own_sum(*args):
    result = 0
    for i in args:
        result += i
    return result


def own_reduce(*args, key: callable, default):
    """
    Aggregates values based on key
    :param args: items to aggregate
    :param key: agg function, receives 2 parameters and returns aggregated value
    :param default: return value if no args are passed
    :return:
    """
    if not args:
        return default
    result = args[0]
    for i in args[1:]:
        result = key(result, i)
    return result

assert own_reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
assert own_reduce(key=mul, default=1) == 1
assert own_reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
assert own_reduce(key=add, default=0) == 0
assert own_sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8
