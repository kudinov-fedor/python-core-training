from akaiafiuk.mine_sweeper import Field
import io
import sys


def test_init():
    field = Field(10, 8, 3)
    assert field.height == 10
    assert field.width == 8
    assert field.field == [["."] * 8 for _ in range(10)]
    assert len(field.mines) == 3


def test_create_mines():
    field = [["."] * 8 for _ in range(10)]
    mines = Field.create_mines(10, field)
    for coord in mines:
        x, y = coord
        assert x <= 8
        assert x >= 0
        assert y <= 10
        assert y >= 0
    assert len(mines) == 10


def test_display_field():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    field = Field(2, 2, 1)
    field.mines = [(0, 0)]
    field.set_sign((1, 1))
    field.set_sign((0, 0))
    field.display_field()
    sys.stdout = sys.__stdout__
    captured_output_as_string = ''.join(e for e in captured_output.getvalue() if e not in "/[]',\n ")
    assert captured_output_as_string == '*..1--'


def test_mines_count():
    field = Field(10, 8, 3)
    field.mines = [(1, 1), (3, 3), (4, 4)]
    assert field.mines_count((2, 2)) == 2
    assert field.mines_count((1, 2)) == 1
    assert field.mines_count((6, 6)) == 0


def test_set_sign():
    field = Field(5, 6, 2)
    field.mines = [(1, 1), (1, 2)]
    field.set_sign((1, 1))
    field.set_sign((2, 2))
    field.set_sign((4, 4))
    assert field.field[1][1] == '*'
    assert field.field[2][2] == '2'
    assert field.field[3][3] == '.'
    assert field.field[4][4] == '0'
