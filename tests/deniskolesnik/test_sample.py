import pytest

"""
Tests for len() python built-in function
Tests for list() python built-in function
"""


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
        result = len(x)
    except Exception as e:
        assert isinstance(e, expected)
    else:
        assert result == expected


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
        result = list(x)
    except Exception as e:
        assert isinstance(e, expected)
    else:
        assert result == expected
