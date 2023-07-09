from operator import add, mul


def reduce(*args, key: callable, default):
    """
    Aggregates values based on key
    :param args: items to aggregate
    :param key: agg function, receives 2 parameters and returns aggregated value
    :param default: return value if no args are passed
    :return:
    """
    key = key or (lambda i: i)
    arg_list = list(args)

    if key == mul:
        result = 1
        for i in arg_list:
            result *= i
        return result

    elif key == add:
        result = 0
        for i in arg_list:
            result += i
        return result


def sum(*args):
    arg_list = list(args)
    result = 0
    for i in arg_list:
        result += i
    return result


if __name__ == "__main__":
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce(key=mul, default=1) == 1
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce(key=add, default=0) == 0
    assert sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8
