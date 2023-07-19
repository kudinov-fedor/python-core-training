
def min(*args, key=None):
    key = key or (lambda i: i)
    return sorted(*args, key=key)[0]


def max(*args, key=None):
    key = key or (lambda i: i)
    return sorted(*args, key=key, reverse=True)[0]


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    # intermediate steps
    key = key or (lambda i: i)
    actual_list = list(args)
    sorted_list = [actual_list[0]]

    sorted_list.insert(0, actual_list[1]) if key(actual_list[1]) < key(sorted_list[0]) else sorted_list.append(actual_list[1])

    # final steps
    for i in range(2, len(actual_list)):
        sorted_len = len(sorted_list)
        last_sorted_item = key(sorted_list[sorted_len - 1])
        first_sorted_item = key(sorted_list[0])

        less_then_first_index = first_sorted_item >= key(actual_list[i])
        more_then_last_index = key(actual_list[i]) >= last_sorted_item

        if less_then_first_index:
            sorted_list.insert(0, actual_list[i])

        elif more_then_last_index:
            sorted_list.insert(sorted_len - 1, actual_list[i]) if actual_list[key(i)] in sorted_list else sorted_list.append(actual_list[i])

        else:
            insert_index = list(j + 1 for j in range(0, sorted_len) if key(sorted_list[j]) <= actual_list[i] < key(sorted_list[j+1]))[0]
            sorted_list.insert(insert_index, key(actual_list[i]))

    return sorted_list[::-1] if reverse else sorted_list
