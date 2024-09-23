def test_lists():
    a = [1, 2, 3]
    b = a

    assert a is b
    assert a == b

    a += [4]

    assert a is b
    assert a == b


def test_strs():
    a = "123"
    b = a

    assert a is b
    assert a == b

    a += "4"
    assert a is not b
    assert a != b

def test_tuples():
    a = (1, 2, 3)
    b = a

    assert a is b
    assert a == b

    a += (4,)

    assert a is not b
    assert a != b