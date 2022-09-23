"""
In this module, test functions verify is subset using issubset() method and "<=" operator.
Scenario #1: Returns True for equal sets
Scenario #2: Returns True if calling from a subset
Scenario #3: Not a subset returns False
Scenario #4: Calling from a bigger set returns False
"""

import pytest


@pytest.mark.parametrize("set_called_from, set_comparing_with, result", [
    ({1, 2, 3}, {1, 2, 3}, True),
    ({1, 2, 3}, {1, 2, 3, 4}, True),
    ({1, 2, 3}, {2, 3, 4}, False),
    ({1, 2, 3, 4}, {1, 2, 3}, False)
])
def test_issubset_method(set_called_from, set_comparing_with, result):
    """Checking issubset() method"""
    assert set_called_from.issubset(set_comparing_with) == result


@pytest.mark.parametrize("set_called_from, set_comparing_with, expected_result", [
    ({1, 2, 3}, {1, 2, 3}, True),
    ({1, 2, 3}, {1, 2, 3, 4}, True),
    ({1, 2, 3}, {2, 3, 4}, False),
    ({1, 2, 3, 4}, {1, 2, 3}, False)
])
def test_issubset_operator(set_called_from, set_comparing_with, expected_result):
    """Checking "<=" operator"""
    actual_result = set_called_from <= set_comparing_with
    assert actual_result == expected_result
