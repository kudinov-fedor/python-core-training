import pytest

from osokolov.guess_word import validate_user_answer, check_win, show_game_result


@pytest.mark.parametrize('data',
                         ['a', 'z'])
def test_validate_user_answer_positive_data(data):
    assert validate_user_answer(data) is True


@pytest.mark.parametrize('negative_data',
                         ['A', 'Z', 'AA', 'ZZZZZZ',
                          1, 0, 99, 1.1, 10000,
                          '.', '\n', ' '])
def test_validate_user_answer_negative_data(negative_data):
    assert validate_user_answer(negative_data) is False


@pytest.mark.parametrize('data', [
    ('abc', ['a', 'b', 'c']),
    ('a', ['a']),
    ('zzzzzzzz', ['z', 'z', 'z', 'z', 'z', 'z', 'z', 'z'])
])
def test_check_win_positive_data(data):
    assert check_win(*data) is True


@pytest.mark.parametrize('data', [
    ('abc', ['a', 'b']),
    ('a', ['c']),
    ('zzzzzzzz', ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']),
    ('xwz', ['a', 'b', 'c'])
])
def test_check_win_negative_data(data):
    assert check_win(*data) is False


@pytest.mark.parametrize('word, list_data, expected_result', [
    ('ab', ['a', 'b'], 'ab'),
    ('ab', ['a', 'c'], 'a*'),
    ('ab', ['c', 'd'], '**')
])
def test_show_game_result(word, list_data, expected_result):
    assert show_game_result(word, list_data) == print(expected_result)
