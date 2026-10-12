# list
def test_list():
    a = [1, 2, 3]
    b = a
    assert a is b
    assert a == b
    assert id(a) == id(b)

    b.append(4)
    assert a is b
    assert a == b
    assert id(a) == id(b)

    b.pop(0)
    assert a is b
    assert a == b
    assert id(a) == id(b)

    a += [4]
    assert a is b
    assert a == b
    assert id(a) == id(b)

# str
def test_string():
    a='123'
    b=a
    assert a is b
    assert a == b
    assert id(a) == id(b)

    a+='4'
    assert a is not b
    assert a != b
    assert id(a) != id(b)

# tuple
def test_tuple():
    a=(1,2,3)
    b=a
    assert a is b
    assert a == b
    assert id(a) == id(b)

    a+=(4,)
    assert a is not b
    assert a != b
    assert id(a) != id(b)
