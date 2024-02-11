def unpack_while_loop(item):
    res = []
    test_list = list(item)
    while test_list:
        current_item = test_list.pop()
        if isinstance(current_item, list):
            test_list.extend(current_item)
        else:
            res.append(current_item)
    return res[::-1]


def unpack_recursive(item):
    flattened_list = []
    for sublist in item:
        if isinstance(sublist, list):
             flattened_list.extend(unpack_recursive(sublist))
        else:
            flattened_list.append(sublist)
    return flattened_list

