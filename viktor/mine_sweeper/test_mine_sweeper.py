import pytest
import game_session as game


@pytest.fixture
def game_session_10(height=10, width=10, mines_count=10):
    return game.GameSession(height, width, mines_count)


@pytest.fixture
def game_session_10_10_3():
    gs = game.GameSession(10, 10, 3)
    gs.mines = [(2, 5), (4, 4), (5, 5)]
    gs.guesses = [(1, 3), (2, 4), (5, 7)]
    return gs


@pytest.fixture
def game_session_2_2_1():
    gs = game.GameSession(2, 2, 1)
    gs.mines = [(0, 0)]
    gs.guesses = [(1, 0), (0, 1)]
    return gs


def test_mines(game_session_10):
    """Should generate exact count of mines"""

    assert len(game_session_10.mines) == 10


@pytest.mark.parametrize("data, expected", [
    ('1 2', (1, 2)),
    (' 2 2 ', (2, 2))
])
def test_normalize_user_input(game_session_10, data, expected):
    """Should return tuple with coordinates"""

    assert game_session_10.normalize_user_input(data) == expected


@pytest.mark.parametrize("data", [
    ("-1 -2"),
    ("a b"),
    ("43 8")
])
def test_normalize_user_input_error(game_session_10, data):
    """Should arise error if data is not correct"""

    with pytest.raises(Exception):
        game_session_10.normalize_user_input(data)


def test_not_open_cells(game_session_2_2_1):
    """Should return correct count of not open cells"""

    assert len(game_session_2_2_1.not_open_cells()) == 1
    assert game_session_2_2_1.not_open_cells() == [(1, 1)]


@pytest.mark.parametrize("coordinates, expected", [((2, 5), True), ((2, 4), False), ((6, 4), False)])
def test_is_mine(game_session_10_10_3, coordinates, expected):
    """Should check if cell with provided coordinates contains mine"""

    assert game_session_10_10_3.is_mine(coordinates) == expected


@pytest.mark.parametrize("coordinates, expected_count", [
    ((3, 5), 2),
    ((0, 0), 0)
])
def test_count_mines_around(game_session_10_10_3, coordinates, expected_count):
    """Should return count of mines around provided coordinates"""

    assert game_session_10_10_3.count_mines_around(coordinates) == expected_count


@pytest.mark.parametrize("coordinates", [
    ((3, 5), (5, 3))
])
def test_save_guess(game_session_10_10_3, coordinates):
    """Should save provided coordinates in 'guesses' array"""

    initial_lenght = len(game_session_10_10_3.guesses)
    game_session_10_10_3.save_guess(coordinates)
    assert coordinates in game_session_10_10_3.guesses
    assert len(game_session_10_10_3.guesses) == initial_lenght + 1


@pytest.mark.parametrize("not_open_cells, expected", [
    ([], True),
    ([(1, 3)], False)
])
def test_win(game_session_2_2_1, not_open_cells, expected):
    """Should check of all cells are open"""

    game_session_2_2_1.not_open_cells = lambda: not_open_cells
    assert game_session_2_2_1.win() == expected