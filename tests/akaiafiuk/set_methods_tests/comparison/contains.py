def test_contains_positive():
    """Returns True if element in set"""
    assert 1 in {1, 2, 3}


def test_contains_negative():
    """Returns False if element not in set"""
    assert 1 not in {2, 3, 4}
