import pytest
from tkupchyn.homework_05.backward_each_word import backward_string_by_word


@pytest.mark.parametrize("given_string, expected_result",
                         [
                             ("", ""),
                             ("world", "dlrow"),
                             ("hello world", "olleh dlrow"),
                             ("hello   world", "olleh   dlrow")

                         ])
def test_backward_string_by_word(given_string, expected_result):
    assert backward_string_by_word(given_string) == expected_result
