
def test_compare_01():
    res = ("d", "o", "g") > ("d", "a", "y")
    assert res is True


def test_compare_02():
    res = (True > False)
    assert res is True