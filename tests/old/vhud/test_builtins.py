def test_min():
    x = [9, 10, 105]
    res = min(x)
    assert res == 9

def test_max():
    x = (10, 15, 125)
    res = max(x)
    assert res == 125

def test_len():
    x = ("Python")
    res = len(x)
    assert res == 6

def test_sum():
    list = [2,3,3,3]
    res = sum(list)
    assert res == 11

def test_float():
    x = "22"
    res = float(x)
    assert res == 22.0

def test_int():
    x = 12.033
    res  = int(x)
    assert res == 12



