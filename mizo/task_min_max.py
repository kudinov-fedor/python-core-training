def test_minimum_custom(*args, key=None):
    if key is None:
        key = lambda a: a
    if not args:
        return None
    minimum = args[0]
    for i in args:
        if key(i) < key(minimum):
            minimum = i
        return minimum


def test_maximum_custom(*args, key=None):
    if key is None:
        key = lambda a: a

    if not args:
        return None

    maximum = args[0]
    for i in args:
        if key(i) > key(maximum):
            maximum = i

    return maximum


def test_minimum_absolute_custom(*args, key=abs):
    if key is None:
        key = lambda a: a
    if not args:
        return None
    minimum = args[0]
    for i in args:
        if key(i) < key(minimum):
            minimum = i
    return minimum


def test_sorted_function(*args, key=None, reverse=False):
    if key is None:
        key = lambda a: a

    if not args:
        return None

    sorted_list = sorted(args, key=key, reverse=False)
    return sorted_list
