def own_max(*args, key=None) -> int:
    result = args[0]
    key = key or (lambda i: i)
    for num in args:
        if key is not None:
            if key(num) > key(result):
                result = num
        elif num > result:
            result = num
    return result


def own_min(*args, key=None) -> int:
    result = args[0]
    key = key or (lambda i: i)
    for num in args:
        if key is not None:
            if key(num) < key(result):
                result = num
        elif num < result:
            result = num
    return result


def own_sort(*args, reverse=False, key=None) -> list:
    my_list = list(args)
    sorted_list = []
    rounds = len(args)

    if key is not None:
        while len(sorted_list) < rounds:
            if reverse:
                x = own_max(*my_list, key=key)
            else:
                x = own_min(*my_list, key=key)
            sorted_list.append(x)
            my_list.remove(x)
    else:
        while len(sorted_list) < rounds:
            if reverse:
                x = own_max(*my_list)
            else:
                x = own_min(*my_list)
            sorted_list.append(x)
            my_list.remove(x)

    return sorted_list
