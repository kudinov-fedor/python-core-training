import pytest


@pytest.mark.parametrize("set_called_from, set_comparing_with, result", [
    ({1, 2, 3}, {1, 2, 3}, True),     # Scenario #1: Returns True for equal sets
    ({1, 2, 3, 4}, {1, 2, 3}, True),  # Scenario #2: Returns True if calling from a superset
    ({1, 2, 3}, {2, 3, 4}, False),    # Scenario #3: Some elements are not common - return False
    ({1, 2, 3}, {1, 2, 3, 4}, False)  # Scenario #4: Calling from a smaller set returns False
])
def test_issubset_method(set_called_from, set_comparing_with, result):
    """Test function verify is superset using issuperset() method."""
    assert set_called_from.issuperset(set_comparing_with) == result


@pytest.mark.parametrize("set_called_from, set_comparing_with, expected_result", [
    ({1, 2, 3}, {1, 2, 3}, True),     # Scenario #1: Returns True for equal sets
    ({1, 2, 3, 4}, {1, 2, 3}, True),  # Scenario #2: Returns True if calling from a superset
    ({1, 2, 3}, {2, 3, 4}, False),    # Scenario #3: Some elements are not common - return False
    ({1, 2, 3}, {1, 2, 3, 4}, False)  # Scenario #4: Calling from a smaller set returns False
])
def test_issubset_operator(set_called_from, set_comparing_with, expected_result):
    """Test function verify is superset using ">=" operator."""
    actual_result = set_called_from >= set_comparing_with
    assert actual_result == expected_result
