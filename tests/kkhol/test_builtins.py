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
    # verify whether r is not empty
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


'''def test_divide_error():
    # Make sure we get error when dividing by 0
    a = 23
    b = 0
    z = a / b

    def func_error():
        with pytest.raises(ZeroDivisionError):
            1 / 0

    assert test_divide_error == func_error


def div_two(a, b) -> ZeroDivisionError:
    return a / b


@pytest.mark.parametrize("a, b, expected", [
    (3, 0, ZeroDivisionError)
])
def test_div_two(a, b, expected):
    assert div_two(a, b) == expected


@pytest.mark.xfail(reason="Expected failure to check division by 0")
def div_two():
    a = 23
    b = 0
    z = a / b
    return z'''


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


def test_isinstance():
    # check whether c is of a particular type
    c = 56
    assert isinstance(c, (int, float, str))
