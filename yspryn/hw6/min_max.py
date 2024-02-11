def min_ysp(*args, key=None):
    res = args[0]
    if key:
        for i in args:
            if key(i) < key(res):
                res = i
    else:
        for i in args:
            if i < res:
                res = i
    return res


def max_ysp(*args, key=None):
    res = args[0]
    if key:
        for i in args:
            if key(i) > abs(res):
                res = i
    else:
        for i in args:
            if i > res:
                res = i
    return res


def sorted_bubbles_method(*args, key=None, reverse=False):
    list_to_sort = list(args)
    stop_mark = True
    if key:
        while stop_mark:
            stop_mark = False
            for i in range(len(list_to_sort) - 1):
                if reverse:
                    temp_var = (list_to_sort[i] if key(list_to_sort[i]) < key(list_to_sort[i + 1]) else None)
                else:
                    temp_var = (list_to_sort[i] if key(list_to_sort[i]) > key(list_to_sort[i + 1]) else None)
                if temp_var is not None:
                    list_to_sort[i] = list_to_sort[i + 1]
                    list_to_sort[i + 1] = temp_var
                    stop_mark = True
    else:
        while stop_mark:
            stop_mark = False
            for i in range(len(list_to_sort) - 1):
                if reverse:
                    temp_var = (list_to_sort[i] if list_to_sort[i] < list_to_sort[i + 1] else None)
                else:
                    temp_var = (list_to_sort[i] if list_to_sort[i] > list_to_sort[i + 1] else None)
                if temp_var is not None:
                    list_to_sort[i] = list_to_sort[i + 1]
                    list_to_sort[i + 1] = temp_var
                    stop_mark = True
    return list_to_sort


def sorted_mim_max_method1(*args, key=None, reverse=False):
    list_to_sort = list(args)
    if reverse:
        if key is None:
            j = 0
            for i in range(j, len(list_to_sort)-1):
                temp_var = max_ysp(*list_to_sort[j:])
                if list_to_sort[j] != temp_var:
                    list_to_sort[list_to_sort.index(temp_var)] = list_to_sort[j]
                    list_to_sort[j] = temp_var
                j += 1
        else:
            j = 0
            for i in range(j, len(list_to_sort) - 1):
                temp_var = (max_ysp(*list_to_sort[j:], key=abs))
                if key(list_to_sort[j]) != temp_var:
                    list_to_sort[list_to_sort.index(temp_var)] = list_to_sort[j]
                    list_to_sort[j] = temp_var
                j += 1
    else:
        if key is None:
            j = 0
            for i in range(j, len(list_to_sort) - 1):
                temp_var = min_ysp(*list_to_sort[j:])
                if list_to_sort[j] != temp_var:
                    list_to_sort[list_to_sort.index(temp_var)] = list_to_sort[j]
                    list_to_sort[j] = temp_var
                j += 1
        else:
            j = 0
            for i in range(j, len(list_to_sort) - 1):
                temp_var = (min_ysp(*list_to_sort[j:], key=abs))
                if key(list_to_sort[j]) != temp_var:
                    list_to_sort[list_to_sort.index(temp_var)] = list_to_sort[j]
                    list_to_sort[j] = temp_var
                j += 1
    print(list_to_sort)
    return list_to_sort
