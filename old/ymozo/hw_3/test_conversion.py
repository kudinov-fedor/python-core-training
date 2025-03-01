import pytest


@pytest.mark.parametrize(["param", "result"], [
    (int("123") == 123, True),
    (int(123.0) == 123.0, True),
    (int("10110101", 2) == 181, True),
    (int("0b10110101", 2) == 181, True),
    (float("123") == 123.0, True),
    (float(123.0) == 123.0, True),
    (float(123) == 123, True),
    (str(123) == "123", True),
    (str(None) == "None", True),
    (list("abc") == ['a', 'b', 'c'], True),
    (list({"a", "b"}) == ['a', 'b'], True),
    (list(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], True),
    (list(enumerate(["a", "b", "c"])) == [(0, 'a'), (1, 'b'), (2, 'c')], True),
    (list(zip(["a", "b", "c"], [1, 2, 3])) == [('a', 1), ('b', 2), ('c', 3)], True),
    (list({"a": 1, "b": 2}.values()) == ([1, 2]), True),
    (list({"a": 1, "b": 2}.items()) == ([('a', 1), ('b', 2)]), True),
    (tuple({"a": 1, "b": 2}) == ('a', 'b'), True),
    (tuple((1, 2, 3)) == (1, 2, 3), True),
    (set("abc") == {'a', 'b', 'c'}, True),
    (set({"a": 1, "b": 2}) == {'a', 'b'}, True),
    (dict(a=123, b=456) == {'a': 123, 'b': 456}, True),
    (dict(enumerate(["a", "b", "c"])) == {0: 'a', 1: 'b', 2: 'c'}, True)
])
def test_conversion(param, result):
    assert param is result
