import pytest

def test_int():
    assert int("123") == int(123.0)
    assert int("10110101", 2) == int("0b10110101", 2)
    assert type(int("10110101", 2)) is type(int("123"))


def test_float():
    assert float("123") == float(123.0)


def test_string():
    assert str(True) in "True Story"
    assert str(None).replace("N", "") == "one"


def test_list():
    assert len(list("abc")) == 3
    assert "".join(reversed("abc")) == "cba"
    assert list({"a": 1, "b": 2}) == ['a', 'b']
    assert list(enumerate(["a", "b", "2"])) == list({0: "a", 1: "b", 2: "2"}.items())
    assert dict(zip(["a", "b", "c"], [2, 1, 3])) == {'a': 2, 'b': 1, 'c': 3}
