
def min(*args, key=None):
    key = key or (lambda i: i)
    min_number, *args = args
    for number in args:
        if key(min_number) is None or key(number) < key(min_number):
            min_number = number
    return min_number


def max(*args, key=None):
    key = key or (lambda i: i)
    max_number, *args = args
    for number in args:
        if key(max_number) is None or key(number) > key(max_number):
            max_number = number
    return max_number


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    sorted_list = []
    default_list = list(args)

    if reverse:
        while default_list:
            maximum = max(*default_list, key=key)
            default_list.remove(maximum)
            sorted_list.append(maximum)
        return sorted_list
    else:
        while default_list:
            for i in default_list:
                minimum = min(*default_list, key=key)
                if i < minimum:
                    minimum = i
            default_list.remove(minimum)
            sorted_list.append(minimum)
        return sorted_list


if __name__ == "__main__":
    assert min(8, -7, -2, 1, 2, 3, 4, 5, 6) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
