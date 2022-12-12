import pytest

from obalk.checkio.upper_all import all_upper, all_upper_upper


@pytest.mark.parametrize("function", [
    all_upper,
    all_upper_upper
])
@pytest.mark.parametrize("text, result", [
    (" ", True),
    ("", True),
    ("4", True),
    ("!", True),
    ("ALL UPPER", True),
    ("UPPER", True),
    ("SOME 54 MIXED 4!# UPPER 81( WITH (@!& NON ()_ ALPHA", True),
    ("all lower", False),
    ("mixed TEXT", False),
])
def test_all_upper(function, text, result):
    assert function(text) == result
