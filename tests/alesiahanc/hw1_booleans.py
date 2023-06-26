import pytest


@pytest.mark.parametrize(["arg1", "expected"], [
    (None, False),  # return False if False, 0 or None
    (False, False),
    (0, False),
    (0.0, False),
    ("", False),
    (set(), False),
    (True, True),  # return True if True, not 0, not empty
    (3, True),
    (-0.1, True),
    ("ab", True),
    ([False, ], True),
    ((None, ), True),
    ({"a": 123}, True)
])
def test_bool_method(arg1, expected):
    result = bool(arg1)
    assert result == expected
