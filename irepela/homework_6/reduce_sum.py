from operator import add


def reduce(*args, key: callable, default):
    """
    Aggregates values based on key
    :param args: items to aggregate
    :param key: agg function, receives 2 parameters and returns aggregated value
    :param default: return value if no args are passed
    :return:
    """
    result = default
    for item in args:
        result = key(result, item)
    return result


# reuse 'reduce' for 'sum' function
def sum(*args):
    return reduce(*args, key=add, default=0)
