# Unpack using while loop
def unpack(item):
    queue = [item]
    result = list()
    while queue:
        x = queue.pop(0)
        if isinstance(x, (list, tuple)):
            queue.extend(x)
        else:
            result.append(x)
    return result


# Unpack using recursion
def unpack(item):
    result = []
    if isinstance(item, int):
        return [item]
    else:
        for x in item:
            result.extend(unpack(x))
    return result


# Unpack with state transition
def unpack(item, result=None):
    result = result or []
    if isinstance(item, int):
        return [item]
    else:
        for x in item:
            if isinstance(x, int):
                result.extend(unpack(x, result=result))
            else:
                result.extend(unpack(x))
    return result


if __name__ == "__main__":
    assert unpack(10) == [10]
    assert unpack([1, 2, 3]) == [1, 2, 3]
    assert unpack([1, [2, 3]]) == [1, 2, 3]
    assert unpack([1, [2, [3]]]) == [1, 2, 3]
    assert unpack([[[[1, 2, 3]]]]) == [1, 2, 3]
