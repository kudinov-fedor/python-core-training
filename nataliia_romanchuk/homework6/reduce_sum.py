from operator import add, mul


def reduce(*args, key: callable, default):
    if not args:
        return default

    agg, *args = args
    for i in args:
        agg = key(agg, i)
    return agg


def sum(*args):
    return reduce(*args, key=add, default=0)
