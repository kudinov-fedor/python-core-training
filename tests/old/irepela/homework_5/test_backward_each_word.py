import pytest
from irepela.homework_5.backward_each_word import backward_each_word


@pytest.mark.parametrize("a, expected", [
    ("", ""),
    ("world", "dlrow"),
    ("hello world", "olleh dlrow"),
    ("hello   world", "olleh   dlrow"),
    ("welcome to a game", "emoclew ot a emag"),
    ("ha ha ha   this is cool", "ah ah ah   siht si looc")

])
def test_backward_each_word(a, expected):
    assert backward_each_word(a) == expected
