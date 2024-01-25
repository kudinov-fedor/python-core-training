def test_list():
    assert list("abc") == ["a", "b", "c"]


def test_empty():
    assert int() == 0
    assert bool() == False
    assert float() == 0.0
    assert str() == ''
    assert tuple() == ()
    assert list() == []
    assert range(10) == range(0, 10)
    assert set() is not ()
    assert dict() == {}


def test_is():
    a = (1, 2, 3)
    b = (1, 2, 3)
    assert a == b
    assert a is b
    hash(a) == hash(b)
    id(a) == id(b)
