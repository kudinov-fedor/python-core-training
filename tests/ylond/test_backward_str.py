import pytest

from ylond.backward_str import backward_string


@pytest.mark.parametrize("text, expected", [
    (" ", " "),
    ("test", "tset"),
    ("1028564", "4658201"),
    ("okko", "okko")])
def test_backward_funct(text, expected):
    assert backward_string(text) == expected

