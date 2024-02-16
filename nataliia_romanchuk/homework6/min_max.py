def minnn(*args, key=None):
    key = key or (lambda i: i)
    res = args[0]
    for i in args:
        if key(i) < key(res):
            res = i
    return res


def min_list(*args):
    min_value = None
    for number in args:
        if number is not None:
            if min_value is None or number < min_value:
                min_value = number
    return min_value


def max_list(*args):
    max_value = None
    for number in args:
        if number is not None:
            if max_value is None or number > max_value:
                max_value = number
    return max_value


def sorted_list(*args, reverse=False):
    sorted_values = []
    arg_list = list(args)
    sort_type = min if reverse == False else max
    while arg_list:
        value = sort_type(arg_list)
        sorted_values.append(value)
        arg_list.remove(value)
    return list(sorted_values)
