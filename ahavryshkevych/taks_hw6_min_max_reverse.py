def max(*args, key=None):
    max_val = 0
    for num in args:
        if num > max_val:
            max_val = num
    return max_val


def min(*args, key=None):
    min_val = 0
    for num in args:
        if key is not None:
            if num < min_val:
                min_val = key(num)
        elif num < min_val:
            min_val = num
    return min_val

def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    my_list = list(args)
    if key is not None and reverse:
        my_list.sort(key=key, reverse=True)
    elif key is not None:
        my_list.sort(key=key)
    elif reverse:
        my_list.sort(reverse=True)
    else:
        my_list.sort()
    return my_list



if __name__ == "__main__":
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
