import pytest

import homework.homework_6.functions
from homework.homework_6 import functions


def test_simple():
    return


assert test_simple() == None


@pytest.mark.parametrize(["param1", "param2", "output"], [
    ["a", "b", ('a', 'b')],
    [1, 2, (1, 2)],
    [{"a": 1, "b": 2}, {"b": 1, "a": 2}, ({'a': 1, 'b': 2}, {'a': 2, 'b': 1})]
])
def test_with_required_params(param1, param2, output):
    assert homework.homework_6.functions.with_required_params(param1, param2) == output


def max_function(*items):
    minimum_value = 0
    for item in list(items):
        for number in item:
            if number > minimum_value:
                minimum_value = number
            else:
                pass
        yield minimum_value


max_function(
    (1, 5, 6, 30, 32, 5, 6, 56),
    (-7, -4, -2, 1, 2, 3, 4, 5, 6),
    (-7, -4, -2, 1, 2, 3, 4, 5, 6),
)
