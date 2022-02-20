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
    #verify whether r is not empty
    r = [9]
    assert len(r) != 0, 'Cannot be empty'


def test_divide():
    #Make sure we do not divide on 0
    a = 23
    b = 7
    z = a / b
    assert b != 0


def test_pres():
    c = '2 few 76 a lot'
    d = '4'
    assert d in c, 'c does not contain d'


# Check is boolean value is a number
def test_bool():
    assert True != 1


def test_bool1():
    assert False != 0, 'False is actually a zero'


def test_alike():
    # Test whether values have similar id's
    a = 4
    b = 4
    c = id(a)
    d = id(b)
    assert c == d


def test_isinstance():
    # check whether c is of a particular type
    c = 56
    assert isinstance(c, (int, float, str))
