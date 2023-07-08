
def min(*args, key=None):
    value_list = args
    min_value = value_list[0]
    for i in value_list:
        if key is not None:
            if key(i) < key(min_value):
                min_value = i
        elif i < min_value:
            min_value = i
    return min_value


def max(*args, key=None):
    value_list = args
    max_value = value_list[0]
    for i in value_list:
        if key is not None:
            if key(i) > key(max_value):
                max_value = i
        elif i > max_value:
            max_value = i
    return max_value


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