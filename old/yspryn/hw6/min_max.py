from operator import lt, gt


def min_ysp(*args, key=None):
    key = key or (lambda i: i)
    res = args[0]
    for i in args:
        if key(i) < key(res):
            res = i
    return res


def max_ysp(*args, key=None):
    key = key or (lambda i: i)
    res = args[0]
    for i in args:
        if key(i) > key(res):
            res = i
    return res


def sorted_bubbles_method(*args, key=None, reverse=False):
    key = key or (lambda i: i)
    compare = lt if reverse else gt
    sorted_list = list(args)
    stop_mark = True
    while stop_mark:
        stop_mark = False
        for i in range(len(sorted_list) - 1):
            temp_var = (sorted_list[i] if compare(key(sorted_list[i]), key(sorted_list[i + 1])) else None)
            if temp_var is not None:
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], temp_var
                stop_mark = True
    return sorted_list


def sorted_mim_max_method(*args, key=None, reverse=False):
    key = key or (lambda i: i)
    input_list = list(args)
    sorted_list = []
    min_or_max = max_ysp if reverse else min_ysp
    while input_list:
        var = min_or_max(*input_list, key=key)
        input_list.remove(var)
        sorted_list.append(var)
    return sorted_list
