import pytest

from ylond.is_acceptable_pass import is_acceptable_pass


@pytest.mark.parametrize("text, expected", [
    ("1 2 5 7", True),
    ("banana ", True),
    ("*******", True),
    ("", False),
    ("test", False),
    ("banana", False)
])
def test_accept_pass(text, expected):
    assert is_acceptable_pass(text) == expected
