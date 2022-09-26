import pytest


@pytest.mark.parametrize("set_called_from, set_comparing_with, expected_result", [
    ({1, 2, 3, 4}, {1, 2, 3}, True),   # Scenario #1: Returns True if calling from a superset
    ({1, 2, 3}, {1, 2, 3}, False),     # Scenario #2: Returns False for equal sets
    ({1, 2, 3}, {1, 2, 3}, False),     # Scenario #3: Returns False if there are uncommon elements
])
def test_more_then(set_called_from, set_comparing_with, expected_result):
    """Basic tests for more then ">" operator"""
    actual_result = set_called_from > set_comparing_with
    assert actual_result == expected_result


@pytest.mark.parametrize("set_called_from, set_comparing_with, expected_result", [
    ({1, 2, 3}, {1, 2, 3, 4}, True),   # Scenario #1: Returns True if calling from a subset
    ({1, 2, 3}, {1, 2, 3}, False),     # Scenario #2: Returns False for equal sets
    ({1, 2, 3}, {1, 2, 3}, False),     # Scenario #3: Returns False if there are uncommon elements
])
def test_less_then(set_called_from, set_comparing_with, expected_result):
    """Basic tests for less then "<" operator"""
    actual_result = set_called_from < set_comparing_with
    assert actual_result == expected_result
