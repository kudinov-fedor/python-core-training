import pytest

from ylond.isdigit_func import isdigit_func


@pytest.mark.parametrize("txt, expected", [
    ("", False),
    ("1 2 5", False),
    ("0.1", False),
    ("\u00B2", True),
    ("\u0030", True),
    ("NULL", False),
    ("5000089999", True),
    ("-1", False)
])
def test_isdigit_funct(txt, expected):
    assert isdigit_func(txt) == expected
