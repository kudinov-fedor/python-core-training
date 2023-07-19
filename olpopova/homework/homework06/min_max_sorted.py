
def min(*args, key=None):
    key = key or (lambda i: i)
    return sorted(*args, key=key)[0]


def max(*args, key=None):
    key = key or (lambda i: i)
    return sorted(*args, key=key, reverse=True)[0]


def sorted(*args, key=None, reverse=False):
    """
    Function sorts data in ASC/DESC order.
    Ascending by default
    """
    key = key or (lambda i: i)

    # final steps
    sorted_list = []
    for i in range(0, len(args)):
        insert_index = identify_insert_index(sorted_list, args[i], key=key)
        sorted_list.insert(insert_index, args[i])

    return sorted_list[::-1] if reverse else sorted_list


def identify_insert_index(collection, item, key=None) -> int:
    """
    Method returns corrected insert index for given item that will be inserted in list
    """
    insert_index = 0

    # edge cases
    if len(collection) == 0 or key(item) < key(collection[0]):
        return insert_index
    elif key(item) > key(collection[-1]):
        insert_index = len(collection)
        return insert_index

    # final steps
    for j in range(0, len(collection)):
        if key(collection[j]) <= key(item) < key(collection[j + 1]):
            insert_index = j + 1
            break

    return insert_index
