from tkupchyn.homework_02.three_words import three_in_row_alternative_solution, three_in_row
import pytest


@pytest.mark.parametrize("text, expected_result", [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("bla 12 bla bla bla", True),
])
def test_three_in_row(text, expected_result):
    assert three_in_row(text) == expected_result


@pytest.mark.parametrize("text, expected_result", [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("bla 12 bla bla bla", True),
])
def test_three_in_row_alternative_solution(text, expected_result):
    assert three_in_row_alternative_solution(text) == expected_result
