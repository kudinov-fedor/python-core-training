import pytest

import homework.homework_6.functions
from anmykh.homework.homework_6 import max_function, min_function, sort_function


@pytest.mark.parametrize(["param1", "param2", "output"], [
    ["a", "b", ('a', 'b')],
    [1, 2, (1, 2)],
    [{"a": 1, "b": 2}, {"b": 1, "a": 2}, ({'a': 1, 'b': 2}, {'a': 2, 'b': 1})]
])
def test_with_required_params(param1, param2, output):
    assert homework.homework_6.functions.with_required_params(param1, param2) == output


@pytest.mark.parametrize(["param", "output"], [
    [[], ValueError],
    [[1], 1],
    [[-1, 0, 3], 3],
    [(""), ValueError],
    [("a"), "a"],
    [("abc"), "c"]
])
def test_max_function(param, output):
    assert max_function(param) == output


@pytest.mark.parametrize(["param", "output"], [
    [[], ValueError],
    [[1], 1],
    [[-1, 0, 3], -1],
    [(""), ValueError],
    [("a"), "a"],
    [("abc"), "a"]
])
def test_min_function(param, output):
    assert min_function(param) == output


@pytest.mark.parametrize(["param", "output"], [
    [[], []],
    [[1], [1]],
    [[0, 2, 8, -1], [-1, 0, 2, 8]],
    [(""), []],
    [("a"), ['a']],
    [("azf"), ['a', 'f', 'z']]
])
def test_sorted(param, output):
    assert sort_function(param) == output
