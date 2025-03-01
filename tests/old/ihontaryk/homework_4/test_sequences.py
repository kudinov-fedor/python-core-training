import pytest

from ihontaryk.homework_4.sequences import check_palindrome_words


@pytest.mark.parametrize('word, expected_result',
                         [('rotator', True),
                          ('level', True),
                          ('banana', False),
                          ('racecar', True)])
def test_check_palindrome_words(word, expected_result):
    """
    verify check_palindrome_words function
    """

    assert check_palindrome_words(word) == expected_result
