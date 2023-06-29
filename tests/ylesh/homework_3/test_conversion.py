import pytest


@pytest.mark.parametrize(["param", "result"], [
    (int("123") == 123, True),
    (str(123.0) == "123.0", True),
    (list("abc") == ['a', 'b', 'c'], True),
    (list({"a": 1, "b": 2}) == ['a', 'b'], True),
    (list(enumerate(["a", "b", "c"])) == [(0, 'a'), (1, 'b'), (2, 'c')], True),
    (list({"a": 1, "b": 2}.keys()) == ['a', 'b'], True),
    (tuple({"a": 1, "b": 2}) == ('a', 'b'), True),
    (set("abc") == {'a', 'c', 'b'}, True),
    (dict(a=123, b=456) == {'a': 123, 'b': 456}, True),
    (dict(zip(["a", "b", "c"], [1, 2, 3])) == {'a': 1, 'b': 2, 'c': 3}, True),
])
def test_assertion(param, result):
    assert param is result
