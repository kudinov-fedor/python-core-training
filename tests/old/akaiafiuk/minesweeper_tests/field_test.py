from akaiafiuk.mine_sweeper import Field


def test_init():
    field = Field(10, 8, 3)
    assert field.height == 10
    assert field.width == 8
    assert field.field == [["."] * 8 for _ in range(10)]
    assert len(field.mines) == 3


def test_create_mines():
    field = Field(10, 8, 10)
    for coord in field.mines:
        assert field.is_coordinate_in_field(coord)
    assert len(field.mines) == 10


def test_mines_count():
    mines = [(1, 1), (3, 3), (4, 4)]
    field = Field(10, 8, mines)
    assert field.mines_count((2, 2)) == 2
    assert field.mines_count((1, 2)) == 1
    assert field.mines_count((6, 6)) == 0


def test_set_sign():
    mines = [(1, 1), (1, 2)]
    field = Field(5, 6, mines)
    field.set_sign((1, 1))
    field.set_sign((2, 2))
    field.set_sign((4, 4))
    assert field.field[1][1] == '*'
    assert field.field[2][2] == '2'
    assert field.field[3][3] == '0'
    assert field.field[4][4] == '0'
    assert field.field[0][0] == '.'


def test_is_mine():
    mines = [(1, 1), ]
    field = Field(5, 6, mines)
    assert field.is_mine((1, 1))
    assert field.is_mine((1, 0)) is False


def test_possible_moves():
    field = Field(2, 2)
    coordinates = [(0, 0), (1, 0), (0, 1), (1, 1)]
    assert field.possible_moves() == coordinates
    for coord in coordinates:
        field.set_sign(coord)
    assert field.possible_moves() == []


def test_empty_cells():
    mines = [(1, 1), ]
    field = Field(5, 6, mines)
    assert (1, 1) in field.possible_moves()
    assert (1, 1) not in field.empty_cells()
