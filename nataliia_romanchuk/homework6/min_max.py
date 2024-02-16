def minnn(*args, key=None):
    key = key or (lambda i: i)
    res = args[0]
    for i in args:
        if key(i) < key(res):
            res = i
    return res


def maxxx(*args, key=None):
    key = key or (lambda i: i)
    res = args[0]
    for i in args:
        if key(i) > key(res):
            res = i
    return res


def sorted_list(*args, reverse=False, key=None):
    sorted_values = []
    arg_list = list(args)
    sort_type = maxxx if reverse else minnn
    while arg_list:
        if key:
            value = sort_type(*arg_list, key=key)
            if value in arg_list:
                arg_list.pop(arg_list.index(value))
                sorted_values.append(value)
        else:
            value = sort_type(*arg_list)
            if value in arg_list:
                arg_list.pop(arg_list.index(value))
                sorted_values.append(value)
    return list(sorted_values)
