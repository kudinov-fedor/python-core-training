def test_is_string():
    assert isinstance("sad", str)


def test_is_set():
    assert isinstance({3, 2, "sad"}, set)


def test_is_tuple():
    assert isinstance((12,5), tuple)

    assert (12) is not tuple


def test_split():
    a = "Hello World"
    b = a.split
    c = " "
    d = b(c)
    e = 0
    f = d[e]
    assert f == "Hello"
