
def unpack_nested(item):
    item = list(item)

    res = []
    while item:
        i = item.pop()
        if isinstance(i, (list, tuple)):
            item.extend(i)
        else:
            res.append(i)
    return res


target = [123, ["234", None], [[1],[23], [[123], 123, ["sdf", True]]]]


print(unpack_nested(target))


def unpack(item, res=None):
    res = [] if res is None else res

    for i in item:
        if isinstance(i, (list, tuple)):
            unpack(i, res=res)
        else:
            res.append(i)

    return res

print(unpack(target))


def unpack(item):
    res = []
    for i in item:
        if isinstance(i, (list, tuple)):
            res.extend(unpack(i))
        else:
            res.append(i)
    return res


print(unpack(target))

