import pytest
import builtins


@pytest.mark.parametrize(["par1", "res"], [
    (lambda: list(zip(["a", "b", "c"], [1, 2, 3])), [("a", 1), ("b", 2), ("c", 3)]),
    (lambda: list(range(10)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (lambda: list({"a": 1, "b": 2}.items()), [('a', 1), ('b', 2)]),
    (lambda: dict(enumerate(['a', 'b', 'c'])), {0: 'a', 1: 'b', 2: 'c'}),
    (lambda: dict({"a": 1, "b": 2}.items()), {'a': 1, 'b': 2}),
    (lambda: dict([("a", 123), ("b", 456)]), {'a': 123, 'b': 456})
])
def test_conversion(par1, res):
    assert par1() == res


@pytest.mark.parametrize(["par2", "res"], [
    (lambda: type([("a", 123), ("b", 456)].__dir__).__name__, "builtin_function_or_method"),
    (lambda: type([("a", 123), ("b", 456)]).__name__, "list"),
    (lambda: type({"a": 1, "b": 2}.items()).__name__, "dict_items")
])
def test_builtins(par2, res):
    assert par2() == res
