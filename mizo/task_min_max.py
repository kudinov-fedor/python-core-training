def minimum_custom(*args, key=None):
    key = key or (lambda a: a)
    if len(args) == 0:
        raise ValueError("empty list")
    minimum = args[0]
    for i in args[1:]:
        if key(i) < key(minimum):
            minimum = i
    return minimum


def maximum_custom(*args, key=None):
    key = key or (lambda a: a)

    if len(args) == 0:
        raise ValueError("empty list")
    maximum = args[0]
    for i in args[1:]:
        if key(i) > key(maximum):
            maximum = i
    return maximum


def my_sorted(*args, key=None, reverse=False):
    """
    Function sorts data in ASC/DESC order.
    Ascending by default
    """

    if len(args) == 0:
        raise ValueError("empty list")

    my_list = list(args)
    sorted_list = []
    num_items = len(args)

    if reverse:
        sort_function = maximum_custom
    else:
        sort_function = minimum_custom

    while len(sorted_list) < num_items:
        item = sort_function(*my_list, key=key)
        sorted_list.append(item)
        my_list.remove(item)
    return sorted_list
