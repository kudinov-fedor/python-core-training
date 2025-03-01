from operator import add, mul


def min(*args, key=None):
    """
    Return min element from scope of value
    @param args: values for min value retrieve
    @param key: if abs retrieve by absolute value
    @returns min_element: Minimum value from scope
    """
    if key is None:
        key = lambda x: x

    min_value = None
    min_element = None
    for element in args:
        value = key(element)
        if min_value is None or value < min_value:
            min_value = value
            min_element = element

    return min_element


def max(*args, key=None):
    """
    Return max element from scope of value
    @param args: values for max value retrieve
    @param key: if abs retrieve by absolute value
    @returns max_element: Maximum value from scope
    """
    if key is None:
        key = lambda x: x

    max_value = None
    max_element = None
    for element in args:
        value = key(element)
        if max_value is None or value > max_value:
            max_value = value
            max_element = element

    return max_element


def sorted(*args, key=None, reverse=False):
    """
    Return sorted elements list
    @param args: values for sort
    @param key: if abs sort by absolute value
    @param reverse: if True return reversed result
    @returns sorted_list: sorted list of values
    """
    items_count = len(args)
    elements = list(args)
    if key is None:
        key = lambda x: x
    sorted_list = []
    for i in range(items_count):
        if reverse:
            value = max(*elements, key=key)
            sorted_list.append(value)
            elements.remove(value)
        else:
            value = min(*elements, key=key)
            sorted_list.append(value)
            elements.remove(value)
    return sorted_list


def reduce(*args, key: callable, default):
    """
    Aggregates values based on key
    :param args: items to aggregate
    :param key: agg function, receives 2 parameters and returns aggregated value
    :param default: return value if no args are passed
    :return result: aggregated result
    """
    if not args:
        result = default
        return result

    result = args[0]
    for i in args[1:]:
        result = key(result, i)
    return result


def sum(*args):
    """
    Sum provided values.
    :param args: values for sum operation
    return sum_result: result of sum operation
    """
    if not args:
        raise SyntaxError("No arguments specified for sum operation")
    sum_result = args[0]
    for i in args[1:]:
        sum_result = sum_result + i
    return sum_result


def unpack_while_loop(item):
    result = []
    while item:
        element = item.pop(0)
        if type(element) is list:
            item = element + item
        else:
            result.append(element)
    return result


def unpack_recursive(item):
    result = []

    def unpack(element):
        if type(element) is list:
            for i in element:
                unpack(i)
        else:
            result.append(element)

    unpack(item)
    return result


def test_min_max():
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]


def test_reduce_sum():
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce(key=mul, default=1) == 1
    assert reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce(key=add, default=0) == 0
    assert sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8


def test_unpack_with_loop():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]


def test_unpack_with_recursive():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
