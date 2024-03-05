import pytest

from operator import add, mul
from homework.homework_6.functions import with_required_params
from anmykh.homework.homework_6_min_max_sort import max_function, min_function, sort_function
from anmykh.homework.homework_6_reduce_sum import reduce_function, sum_function
from anmykh.homework.homework_6_unpack import unpack_while_loop, unpack_recursive


@pytest.mark.parametrize(["param1", "param2", "output"], [
    ["a", "b", ('a', 'b')],
    [1, 2, (1, 2)],
    [{"a": 1, "b": 2}, {"b": 1, "a": 2}, ({'a': 1, 'b': 2}, {'a': 2, 'b': 1})]
])
def test_with_required_params(param1, param2, output):
    assert with_required_params(param1, param2) == output


@pytest.mark.parametrize(["param", "output"], [
    [[1], 1],
    [[-1, 0, 3], 3],
    [("a"), "a"],
    [("abc"), "c"]
])
def test_max_function(param, output):
    assert max_function(param) == output


@pytest.mark.parametrize("func", [
    min_function,
    max_function
])
@pytest.mark.parametrize(["param"], [
    [[]],
    [("")]
])
def test_max_function_failure(func, param):
    with pytest.raises(ValueError):
        assert func(param)


@pytest.mark.parametrize(["param", "output"], [
    [[1], 1],
    [[-1, 0, 3], -1],
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


def test_reduce_sum():
    assert reduce_function(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1) == -40320
    assert reduce_function(key=mul, default=1) == 1
    assert reduce_function(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=add, default=0) == 8
    assert reduce_function(key=add, default=0) == 0
    assert sum_function(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8


def test_unpack():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
