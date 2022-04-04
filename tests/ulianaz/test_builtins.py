

def test_len():
    x = "j,h,b,b,v,k,b,h,3,4"
    res = len(x)
    y = list(x)
    print(y)
    assert res == 19


def test_len_list():
    x = [1, 2, 3, 4]
    res = len(x)
    assert res == 4
