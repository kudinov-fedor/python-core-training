
def unpack_while_loop(item):
    queue = list(item)

    res = []
    while queue:
        i = queue.pop()
        if isinstance(i, (list, tuple)):
            queue.extend(i)
        else:
            res.append(i)
    return res[::-1]


def unpack_recursive(item):
    res = []
    for i in item:
        if isinstance(i, (list, tuple)):
            res.extend(unpack_recursive(i))
        else:
            res.append(i)
    return res
