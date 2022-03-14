import pytest


def test_len():
    x = "23456"
    res = len(x)
    assert res == 5


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


def test_len3():
    # verify whether r is not empty
    r = [9]
    assert len(r) != 0, 'Cannot be empty'


def test_divide():
    # Make sure we do not divide on 0
    a = 23
    b = 7
    assert b != 0
    z = a / b


#Make sure we get error during division by 0
def test_divide2():
    a = 23
    b = 0
    with pytest.raises(ZeroDivisionError):
        var = a / b

a = 4
b = 0


def error_func():
    a / b  # causes ZeroDivisionError


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
    a = 4
    b = 4
    c = id(a)
    assert c == id(a)
    d = id(b)
    assert d == id(b)
    assert c == d
    assert a == b
   

def test_isinstance():
    # check whether c is of a particular type
    c = 56
    assert isinstance(c, (int, float, str))
