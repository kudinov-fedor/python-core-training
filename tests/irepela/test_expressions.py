def test_equality():
    assert id(str.join) != id("".join)


def test_joins():
    assert str.join("|", "abc") == "|".join("abc")


def test_split():
    a, b = "Hello World".split(" ")
    assert a == "Hello"
    assert b == "World"
