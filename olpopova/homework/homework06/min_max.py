
def min(*args, key=None):
    key = key or (lambda i: i)
    # list1 = []
    # for i in args:
    #     list1.append(key_value(i))
    return sorted(*args, key=key)[0]


def max(*args, key=None):
    key = key or (lambda i: i)
    # list1 = []
    # for i in args:
    #     list1.append(key_value(i))
    return sorted(*args, key=key, reverse=False)[0]


def sorted(*args, key=None, reverse=False):
    """Ascending by default"""
    # intermediate steps
    key = {key: key or (lambda i: i),
              reverse: key or (lambda i: i)
              }[key]
    list1 = list(args)
    sorted_list = []

    sorted_list.append(key(list1[0]))
    sorted_list.insert(0, key(list1[1])) if list1[1] < sorted_list[0] else sorted_list.append(key(list1[1]))

    for i in range(2, len(list1)):
        # edge cases:
        if list1[i] not in sorted_list:
            less_then_first_index = list1[i] < sorted_list[0]
            more_then_last_index = sorted_list[len(sorted_list) - 1] < list1[i]
            if less_then_first_index:
                sorted_list.insert(0, key(list1[i]))
            elif more_then_last_index:
                sorted_list.append(key(list1[i]))
            else:
                insert_index = list(j + 1 for j in range(0, len(sorted_list)) if sorted_list[j] < list1[i] < sorted_list[j+1])[0]
                # if is_input_index_found:
                sorted_list.insert(insert_index, key(list1[i]))
    return sorted_list


if __name__ == "__main__":
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7      #
    # assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, 4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1   #
    assert sorted(6, 1, -2, -4, -7) == [-7, -4, -2, 1, 6]
    assert sorted(-1, 122, 9, 7, 56, 0) == [-1, 0, 7, 9, 56, 122]
