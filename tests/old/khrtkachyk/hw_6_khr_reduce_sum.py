from operator import add, mul


def reduce_func(*args, key: callable, default):
    """
    Aggregates values based on key
    :param args: items to aggregate
    :param key: agg function, receives 2 parameters and returns aggregated value
    :param default: return value if no args are passed
    :return:
    """
    value = default
    if len(args) == 0:
        return value
    for i in args:
        value = key(value, i)
    return value


def sum_func(*args):
    if len(args) == 0:
        return 0
    value = 0
    for i in args:
        value += i
    return value


def sum_func_2_0(*args):
    if len(args) == 0:
        return 0
    res = 0
    for i in args:
        res = add(i, res)
    return res
