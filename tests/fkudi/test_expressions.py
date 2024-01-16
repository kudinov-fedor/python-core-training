
def test_list_check():

    a = [1, 2, 3]
    b = a

    assert id(a) == id(b)

    a += [4]
    assert id(a) == id(b)

    assert a is b
    assert a == b


def test_tuple_check():
    a = (1, 2, 3)
    b = a

    assert id(a) == id(b)

    a += (4,)
    assert id(a) != id(b)

    assert a is not b
    assert a != b
