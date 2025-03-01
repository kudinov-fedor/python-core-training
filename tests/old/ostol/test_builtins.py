def test_min():
    x = (1,2,3,4)
    res = min(x)
    assert res == 1

def test_min_list():
    x = [1, 2, 3, 4]
    res = min(x)
    assert res == 1

def test_max():
    x = (1, 2, 3, 4)
    res = max(x)
    assert res == 4

def test_max_list():
    x = [1, 2, 3, 4]
    res = max(x)
    assert res == 4

def test_abs():
    x = -6.678
    res = abs(x)
    assert res == 6.678

def test_all_True():
    x = [True, True, True]
    res = all(x)
    assert res == True

def test_all_False():
    x = [True, True, False]
    res = all(x)
    assert res == False

def test_any_True():
    x = [True, False, False]
    res = any(x)
    assert res == True

def test_any_False():
    x = [False, False, False]
    res = any(x)
    assert res == False

def test_bin():
    x = 76
    res = bin(x)
    assert res == '0b1001100'

def test_bool_True():
    x = 1.23
    res = bool(x)
    assert res == True

def test_bool_False():
    x = []
    res = bool(x)
    assert res == False

def test_bytearray():
    x = 4
    res = bytearray(x)
    assert res == bytearray(b'\x00\x00\x00\x00')

def test_bytes():
    x = 6
    res = bytes(x)
    assert res == b'\x00\x00\x00\x00\x00\x00'
