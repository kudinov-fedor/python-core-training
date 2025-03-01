def custom_min(*args, key=None):
    """
    Function to find minimal value
    """

    key = key or (lambda i: i)
    result, *args = args

    for arg in args:
        if key(arg) < key(result):
            result = arg

    return result


def custom_max(*args, key=None):
    """
    Function to find maximal value
    """

    key = key or (lambda i: i)
    result, *args = args

    for arg in args:
        if key(arg) > key(result):
            result = arg
    return result


def custom_sorted(*args, key=None, reverse=False):
    """
    Function to sort in ASC and DESC order
    ASC by default
    """

    sorted_list = []
    func = custom_max if reverse else custom_min

    assert args
    args = list(args)

    while args:
        element = func(*args, key=key)
        args.remove(element)
        sorted_list.append(element)
    return sorted_list


if __name__ == "__main__":
    print(custom_sorted(-7, -4, -2, 1, 6, 2, 3, 4, 5, 8, 7))
