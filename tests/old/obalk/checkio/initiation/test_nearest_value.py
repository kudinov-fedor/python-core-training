import pytest

from obalk.checkio.initiation.nearest_value import nearest_value, nearest_value_lambda, nearest_value_with_nested_func


@pytest.mark.parametrize("function", [
   nearest_value,
   nearest_value_lambda,
   nearest_value_with_nested_func
])
@pytest.mark.parametrize("values, one, result", [
    ({100, 5, 8, 10, 12, 89}, 7, 8),
    ({0, -2}, -1, -2),
    ({5}, 5, 5)
])
def test_nearest_value(function, values, one, result):
    assert function(values, one) == result
