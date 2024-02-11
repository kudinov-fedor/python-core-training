def reduce(*args, key: callable, default):
    if args:
        res = None
        for i in args:
            if res is None:
                res = i
            else:
                res = key(res, i)
        return res
    else:
        return default


def sum(*args):
    res = 0
    for i in args:
        res += i
    return res
