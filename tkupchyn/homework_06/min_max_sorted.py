def custom_max(*collection, key: callable = None) -> (int, float, str):
    """
    Takes a variable number of arguments and optionally a key function, and then return the maximum value
    based on the provided key

    Args:
        collection: a number of arguments of one type than can be compared
        key (callable): A function to be applied to the elements of the collection
        to determine the maximum value
    Returns:
        (int, float, str): The maximum value
    """
    max_val, *collection = collection
    key = key or (lambda i: i)

    for elem in collection:
        if key(elem) > key(max_val):
            max_val = elem
    return max_val


def custom_min(*collection, key: callable = None) -> (int, float, str):
    """
    Takes a variable number of arguments and optionally a key function, and then return the minnimun value
    based on the provided key

    Args:
        collection: a number of arguments of one type than can be compared
        key (callable): A function to be applied to the elements of the collection
        to determine the minimum value
    Returns:
        (int, float, str): The minimum value
    """
    min_val, *collection = collection
    key = key or (lambda i: i)

    for elem in collection:
        if key(elem) < key(min_val):
            min_val = elem

    return min_val


def custom_sorted(*collection, reverse=None, key: callable = None) -> list:
    """
    Takes a variable number of arguments and optionally a key function, and then return the sorted collection

    Args:
    collection: a number of arguments of one type than can be compared
    reverse (bool, optional): If True, the collection is sorted in descending order.
    If False or None, the collection is sorted in ascending order. Default is None.
    key (callable, optional): A function to be applied to the elements of the collection

    Returns:
        (list): The sorted list of arguments from collection
    """
    collection = list(collection)
    sorted_list = []

    func = custom_max if reverse else custom_min

    while collection:
        elem = func(*collection, key=key)
        collection.remove(elem)
        sorted_list.append(elem)

    return sorted_list
