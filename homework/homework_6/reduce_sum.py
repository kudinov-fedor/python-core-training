from operator import add, mul


def reduce(*args, key: callable, default):
    """
    Aggregates values based on key
    :param args: items to aggregate
    :param key: agg function, receives 2 parameters and returns aggregated value
    :param default: return value if no args are passed
    :return:
    """
    return 0


# reuse 'reduce' for 'sum' function
def sum(*args):
    return 0


if __name__ == "__main__":
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce(key=mul, default=1) == 1
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce(key=add, default=0) == 0
    assert sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8
