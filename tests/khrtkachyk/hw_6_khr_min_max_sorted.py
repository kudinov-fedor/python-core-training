def minimum(*args, key=None):
    key = key or (lambda a: a)
    if len(args) == 0:
        raise ValueError("min() arg is an empty sequence")
    minimal = args[0]
    for i in args[1:]:
        if key(i) < key(minimal):
            minimal = i
    return minimal


def maximum(*args, key=None):
    key = key or (lambda a: a)
    if len(args) == 0:
        raise ValueError("max() arg is an empty sequence")
    maximal = args[0]
    for i in args[1:]:
        if key(i) > key(maximal):
            maximal = i
    return maximal


def sorting(*args, key=None, reverse=False):
    """Ascending by default"""

    lst = list(args)
    key = key or (lambda a: a)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if key(lst[j]) < key(lst[i]):
                lst[j], lst[i] = lst[i], lst[j]
    return lst[::-1] if reverse == True else lst
