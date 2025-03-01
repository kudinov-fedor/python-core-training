import pytest
from ybilyn.first_word import first_word


@pytest.mark.parametrize("text, expected", [
    ("Hello world", "Hello"),
    ("Hello_world", "Hello_world"),
    ("Helloworld one more time", "Helloworld"),
])
def test_first_word(text, expected):
    assert first_word(text) == expected
