def type_error():
    return {1, 2} + {3}


def key_error():
    data = {1: 0}
    return data[2]


def index_error():
    a = "12345"
    return a[len(a) + 1]


def name_error(a):
    for i in c:
        print(i)


def attribute_error():
    6 / 2


def assertion_error():
    a = ""
    assert isinstance(a, list)
