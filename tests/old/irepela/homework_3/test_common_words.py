import pytest
from irepela.homework_3.common_words import get_common_words_sol_1, get_common_words_sol_2


@pytest.mark.parametrize("a, b, expected", [
    ("hello,world", "hello,earth", "hello"),
    ("one,two,three", "four,five,six", ""),
    ("one,two,three", "four,five,one,two,six,three", "one,three,two")
])
def test_common_words(a, b, expected):
    assert get_common_words_sol_1(a, b) == expected
    assert get_common_words_sol_2(a, b) == expected
