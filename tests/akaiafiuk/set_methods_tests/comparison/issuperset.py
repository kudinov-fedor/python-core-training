"""
In this module, test functions verify is superset using issuperset() method and ">=" operator.
Long story short: True if calling from equal or bigger set.
Scenario #1: Returns True for equal sets
Scenario #2: Returns True if calling from a superset
Scenario #3: Some elements are not common - return False
Scenario #4: Calling from a smaller set returns False
"""

import pytest


@pytest.mark.parametrize("set_called_from, set_comparing_with, result", [
    ({1, 2, 3}, {1, 2, 3}, True),
    ({1, 2, 3, 4}, {1, 2, 3}, True),
    ({1, 2, 3}, {2, 3, 4}, False),
    ({1, 2, 3}, {1, 2, 3, 4}, False)
])
def test_issubset_method(set_called_from, set_comparing_with, result):
    """Checking issubset() method"""
    assert set_called_from.issuperset(set_comparing_with) == result


@pytest.mark.parametrize("set_called_from, set_comparing_with, expected_result", [
    ({1, 2, 3}, {1, 2, 3}, True),
    ({1, 2, 3, 4}, {1, 2, 3}, True),
    ({1, 2, 3}, {2, 3, 4}, False),
    ({1, 2, 3}, {1, 2, 3, 4}, False)
])
def test_issubset_operator(set_called_from, set_comparing_with, expected_result):
    """Checking "<=" operator"""
    actual_result = set_called_from >= set_comparing_with
    assert actual_result == expected_result
