# Unpack using while loop
def unpack_while(item):
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
def unpack_recursion(item):
    result = []
    if isinstance(item, int):
        return [item]
    else:
        for x in item:
            result.extend(unpack_recursion(x))
    return result


# Unpack with state transition
def unpack_recursion_state_transition(item, result=None):
    result = result if result is not None else []
    if isinstance(item, int):
        result.append(item)
    else:
        for x in item:
            unpack_recursion_state_transition(x, result=result)
    return result
