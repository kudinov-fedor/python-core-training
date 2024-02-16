import pytest

import homework.homework_6.functions
from anmykh.homework.homework_6 import max_function

@pytest.mark.parametrize(["param1", "param2", "output"], [
    ["a", "b", ('a', 'b')],
    [1, 2, (1, 2)],
    [{"a": 1, "b": 2}, {"b": 1, "a": 2}, ({'a': 1, 'b': 2}, {'a': 2, 'b': 1})]
])
def test_with_required_params(param1, param2, output):
    assert homework.homework_6.functions.with_required_params(param1, param2) == output


@pytest.mark.parametrize(["param", "output"], [
    [(-7, -4, -2, 1, 2, 3, 4, 5, 6), 6],
    [(2, 4, 9, 11, 100), 100],
    [(0, 0, 3, 89, 10, 11), 89]
])
def test_max_function(param, output):
    assert max_function(param) == output
