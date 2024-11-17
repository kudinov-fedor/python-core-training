from operator import add, mul


def reduce(*args, key: callable, default):
    """
    Aggregates values based on key
    :param args: items to aggregate
    :param key: agg function, receives 2 parameters and returns aggregated value
    :param default: return value if no args are passed
    :return:
    """
    if not args:
        return default

    key = key or (lambda x: x)
    args_copy = list(args)
    while len(args_copy) > 1:
        args_copy.append(key(args_copy.pop(0), args_copy.pop(0)))
    return args_copy[0]


# reuse 'reduce' for 'sum' function
def sum(*args):
    return reduce(*args, key=add, default=0)
