from operator import add


def reduce(*args, key: callable, default):
    if not args:
        return default
    res = None
    for i in args:
        if res is None:
            res = i
        else:
            res = key(res, i)
    return res


def sum(*args):
    return reduce(*args, key=add, default=0)
