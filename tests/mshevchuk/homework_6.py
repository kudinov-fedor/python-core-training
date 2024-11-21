from operator import add, mul


def check_args(args):
    if not args:
        raise ValueError("arg is an empty sequence")


def min(*args, key=None):
    check_args(args)
    key = key or (lambda i: i)
    min_value = args[0]
    for i in args[1:]:
        if key(i) < key(min_value):
            min_value = i
    return min_value


def max(*args, key=None):
    check_args(args)
    key = key or (lambda i: i)
    max_value = args[0]
    for i in args[1:]:
        if key(i) > key(max_value):
            max_value = i
    return max_value


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    check_args(args)
    func = max if reverse else min
    args = list(args)
    new_list = list()
    while args:
        value = func(*args, key=key)
        new_list.append(value)
        args.remove(value)
    return new_list


def reduce(*args, key: callable, default):
    if args:
        key = key or (lambda i: i)
        value = args[0]
        for i in args[1:]:
            value = key(value, i)
        return value
    else:
        return default


def sum(*args):
    check_args(args)
    sum = 0
    for i in args:
        sum += i
    return sum


if __name__ == "__main__":
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == -7
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce(key=mul, default=1) == 1
    print("here : ", reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0))
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce(key=add, default=0) == 0
    assert sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8
