import pytest
from tkupchyn.homework_03.the_most_wanted_letter import find_most_frequent_letter


@pytest.mark.parametrize("phrase, expected",
                         [
                             ("Hello World!,,,,,,,,,,,,", "l"),
                             ("Hello World!", "l"),
                             ("One", "e"),
                             ("One asd sadsadsadjkadjsdsjjjjjjjjjjjjjjjjjjjjj", "j"),
                             ("Oops 1111111", "o")
                         ])
def test_most_wanted_letter(phrase, expected):
    assert find_most_frequent_letter(phrase) == expected
