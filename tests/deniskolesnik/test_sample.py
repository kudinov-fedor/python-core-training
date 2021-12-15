import pytest

"""
Tests for len() python built-in function
Tests for list() python built-in function
"""


def len_func(x):
    return len(x)


def list_func(x):
    return list(x)


@pytest.mark.parametrize("x, expected", [
    (5, TypeError),
    (5.0, TypeError),
    (0, TypeError),
    (None, TypeError),
    ('', 0),
    ('hello', 5),
])
def test_len(x, expected):
    try:
        assert len_func(x) == expected
    except TypeError:
        pass
    else:
        return AssertionError


@pytest.mark.parametrize("x, expected", [
    (5, TypeError),
    (5.0, TypeError),
    (0, TypeError),
    (None, TypeError),
    ('', []),
    ('hello', ['h', 'e', 'l', 'l', 'o']),
])
def test_list(x, expected):
    try:
        assert list_func(x) == expected
    except TypeError:
        pass
    else:
        return AssertionError
