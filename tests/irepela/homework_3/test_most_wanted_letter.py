import pytest
from irepela.homework_3.most_wanted_letter import get_most_wanted_letter


@pytest.mark.parametrize("a, expected", [
    ("Hello World!", "l"),
    ("How do you do?", "o"),
    ("One", "e"),
    ("Oops!", "o"),
    ("AAaooo!!!!", "a"),
    ("abe", "a")
])
def test_most_wanted_letter(a, expected):
    assert get_most_wanted_letter(a) == expected
