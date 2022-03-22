import pytest


def test_len():
    x = "23456"
    res = len(x)
    assert res == 5
    assert x


@pytest.mark.parametrize("item, expected_length", [
    ("23456", 5),
    ([1, 2, 3, 6, 8], 5),
    ([], 0)
])
def test_len_list_various_types(item, expected_length):
    x = item
    res = len(x)
    assert res == expected_length


def test_len_error():
    x = 145
    with pytest.raises(TypeError):
        len(x)


def test_len2():
    # verify whether length of r is not zero
    r = [34, 56, 87, 23]
    assert len(r) != 0
    assert r != 0
    assert r


def test_len3():
    # verify whether r is not empty
    r = [9]
    assert len(r) != 0, 'Cannot be empty'


def test_divide():
    # Make sure z is not 0
    a = 23
    b = 7
    z = a / b
    assert z != 0


# Make sure we get error during division by 0
def test_divide2():
    a = 23
    b = 0
    with pytest.raises(ZeroDivisionError):
        var = a / b


def error_func():
    a = 4
    b = 0
    var = a / b  # causes ZeroDivisionError


def test_error_func():
    try:
        error_func()
        print("bla bla bla")
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Error did not happen")


def test_error_func_2():
    with pytest.raises(ZeroDivisionError):
        error_func()


def test_pres():
    c = '2 few 764 a lot'
    d = '4'
    assert d in c


# Check is boolean value is a number
def add_bool(a: int, b: bool) -> int:
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (3, True, 4),
    (4, False, 4),
])
def test_add_bool(a, b, expected):
    assert add_bool(a, b) == expected


def test_bool1():
    assert False == 0


@pytest.mark.xfail(reason="Expected failure to check False case")
def test_bool2():
    assert False != 0, 'False is actually a zero'


def test_alike():
    # Test whether values have similar id's
    a = 256
    b = 256
    assert id(a) == id(b)
    c = id(a)
    assert c == id(a)
    d = id(b)
    assert d == id(b)
    assert c == d
    assert a == b


def test_not_alike():
    param1 = 257
    param2 = 256
    assert id(param1) != id(param2)
    assert param1 != param2


def test_isinstance():
    # check whether c is of a particular type
    c = 'norway'
    assert isinstance(c, (int, float, str))
    assert not isinstance(c, (float, int))
    c1 = 87.9
    assert isinstance(c1, (int, float, str))
    assert not isinstance(c1, (int, str))
    c2 = 45
    assert isinstance(c2, (int, float, str))
    assert not isinstance(c2, (float, str))
