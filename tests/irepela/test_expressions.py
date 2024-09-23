def test_equality():
    assert id(str.join) != id("".join)


def test_joins():
    assert str.join("|", "abc") == "|".join("abc")


def test_split():
    splitted = "Hello World".split(" ")
    assert splitted[0] == "Hello"
    assert splitted[1] == "World"
