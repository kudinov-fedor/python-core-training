
def min(*args, key=None):
    result, *args = args
    key = key or (lambda i: i)
    for i in args:
        if key(i) < key(result):
            result = i
    return result


def max(*args, key=None):
    result, *args = args
    key = key or (lambda i: i)
    for i in args:
        if key(i) > key(result):
            result = i
    return result


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    sorted_list = []

    func = max if reverse else min
    arg_list = list(args)

    while arg_list:
        item = func(*arg_list, key=key)
        arg_list.remove(item)
        sorted_list.append(item)
    return sorted_list


if __name__ == "__main__":
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]