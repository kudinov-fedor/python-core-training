import pytest
import game_session as game

a, b, c = 10, 10, 10


def test_mines():
    game_session = game.GameSession(a, b, c)
    assert len(game_session.mines) == c


test_data = [
    ('4 7', (4, 7)),
    (' 5 8 ', (5, 8))
]


@pytest.mark.parametrize("data, expected", test_data)
def test_normalize_user_input(data, expected):
    game_session = game.GameSession(a, b, c)

    assert game_session.normalize_user_input(data) == expected


test_data_error = [
    ("-1, -2", "OutOfBounds"),
    ("a b", "ValueError")
]


@pytest.mark.parametrize("data, error_message", test_data_error)
def test_normalize_user_input_error(data, error_message):
    game_session = game.GameSession(a, b, c)

    with pytest.raises(Exception) as error:
        game_session.normalize_user_input(data)
        assert str(error.value) == error_message


def test_not_open_cells():
    c = 3

    game_session = game.GameSession(a, b, c)
    game_session.mines = [(1, 4), (2, 5), (3, 7)]
    game_session.guesses = [(1, 3), (2, 4), (5, 7)]
    # mocked_guesses = list(filter(lambda coordinates: coordinates not in game_session.mines, [(1, 3), (2, 4), (5, 7)]))
    # game_session.guesses.extend(mocked_guesses)
    assert len(game_session.not_open_cells()) == a * b - c - len(game_session.guesses)


test_coordinates = [((1, 4), True), ((2, 4), False), ((6, 4), False)]


@pytest.mark.parametrize("coordinates, expected", test_coordinates)
def test_is_mine(coordinates, expected):
    c = 3

    game_session = game.GameSession(a, b, c)
    game_session.mines = [(1, 4), (2, 5), (3, 7)]
    assert game_session.is_mine(coordinates) == expected


test_coordinates = [
    ((3, 5), [(2, 5), (4, 4), (5, 5)], 2),
    ((4, 4), [(2, 5), (1, 1), (5, 7)], 0)
]


@pytest.mark.parametrize("coordinates, mines, expected_count", test_coordinates)
def test_count_mines_around(coordinates, mines, expected_count):
    c = 3

    game_session = game.GameSession(a, b, c)
    game_session.mines = mines
    assert game_session.count_mines_around(coordinates) == expected_count


test_coordinates_guess = [
    ((3, 5), (5, 3))
]


@pytest.mark.parametrize("coordinates", test_coordinates_guess)
def test_save_guess(coordinates):
    c = 3

    game_session = game.GameSession(a, b, c)
    initial_lenght = len(game_session.guesses)
    game_session.save_guess(coordinates)
    # assert len(game_session.guesses) == initial_lenght + 1
    pytest.assume(coordinates in game_session.guesses)
    pytest.assume(len(game_session.guesses) == initial_lenght + 1)


test_params = [
    ([], True),
    ([(1, 3)], False)
]


@pytest.mark.parametrize("not_open_cells, expected", test_params)
def test_win(not_open_cells, expected):
    a = 3
    b = 3
    c = 2

    game_session = game.GameSession(a, b, c)
    game_session.not_open_cells = lambda: not_open_cells
    assert game_session.win() == expected
