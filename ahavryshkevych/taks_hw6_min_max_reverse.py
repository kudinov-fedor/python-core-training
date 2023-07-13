def own_max(*args, key=None) -> int:
    result = args[0]
    key = key or (lambda i: i)
    for num in args:
        if key(num) > key(result):
            result = num
    return result


def own_min(*args, key=None) -> int:
    result = args[0]
    key = key or (lambda i: i)
    for num in args:
        if key(num) < key(result):
            result = num
    return result


def own_sort(*args, reverse=False, key=None) -> list:
    my_list = list(args)
    sorted_list = []
    rounds = len(args)

    if reverse:
        func = own_max
    else:
        func = own_min

    while len(sorted_list) < rounds:
        item = func(*my_list, key=key)
        sorted_list.append(item)
        my_list.remove(item)
    return sorted_list
