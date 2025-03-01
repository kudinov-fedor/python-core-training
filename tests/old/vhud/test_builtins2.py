def test_min():
    x = [9, 10, 105]
    res = min(x)
    assert res == 9


def test_max():
    x = (10, 15, 125)
    res = max(x)
    assert res == 125


def test_len():
    x = "Python"
    res = len(x)
    assert res == 6


def test_sum():
    list = [2, 3, 3, 3]
    res = sum(list)
    assert res == 11


def test_float():
    x = "22"
    res = float(x)
    assert res == 22.0


def test_int():
    x = 12.033
    res = int(x)
    assert res == 12


def test_abs():
    x = -100
    res = abs(x)
    assert res == 100


def test_all():
    mylist = []
    res = all(mylist)
    assert res == True


def test_any():
    x = (1, 0, 5)
    res = any(x)
    assert res == True


def test_bool():
    x = {}
    res = bool(x)
    assert res == False


def test_callable():
    x = 105
    res = callable(x)
    assert res == False


def test_dict():
    x = dict(coffee="latte", coffee1="espresso")
    res = dict(x)
    assert res == {'coffee': 'latte', 'coffee1': 'espresso'}


def test_enumerate():
    x = ("dog", "cat", "cow")
    res = enumerate(x)
    assert res == [(0, "dog"), (1, "cat"), (2, "cow")]
