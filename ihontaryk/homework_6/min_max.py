def custom_min(*args, key=None):
    key = key or (lambda i: i)
    res, *args = args

    for i in args:
        if key(i) < key(res):
            res = i
    return res


def custom_max(*args, key=None):
    key = key or (lambda i: i)
    res, *args = args

    for i in args:
        if key(i) > key(res):
            res = i
    return res


def custom_sorted(*args, key=None, reverse=False):
    """
    min/max sort to reuse min/max function
    Ascending by default
    """
    sorted_list = []
    func = custom_max if reverse else custom_min

    assert args
    args = list(args)
    while args:
        item = func(*args, key=key)
        args.remove(item)
        sorted_list.append(item)
    return sorted_list


if __name__ == "__main__":
    print(custom_sorted(-7, -4, -2, 1, 6, 2, 3, 4, 5, 8, 7))
