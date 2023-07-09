
def min(*args, key=None):
    key = key or (lambda i: i)
    min_number, *args = args

    for number in args:
        if key(number) < key(min_number):
            min_number = number
    return min_number


def max(*args, key=None):
    key = key or (lambda i: i)
    max_number, *args = args

    for number in args:
        if key(number) > key(max_number):
            max_number = number
    return max_number


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    sorted_list = []
    default_list = list(args)
    func = max if reverse else min

    while default_list:
        min_max_number = func(*default_list, key=key)
        default_list.remove(min_max_number)
        sorted_list.append(min_max_number)
    print(sorted_list)
    return sorted_list


if __name__ == "__main__":
    assert max(1,2,3,4,99,12,15,123, key=str) == 99
    assert min(8, -7, -2, 1, 2, 3, 4, 5, 6) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
    assert sorted(1,2,3,4,99,12,15,123, key=str) == [1, 12, 123, 15, 2, 3, 4, 99]
