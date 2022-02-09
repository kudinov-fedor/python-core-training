from akaiafiuk.mine_sweeper.controllers import next_move_user, next_move_automatic
from akaiafiuk.mine_sweeper import controllers
from akaiafiuk.mine_sweeper import Field


def test_next_move_automatic(mocker):
    mocker.patch.object(controllers, 'randint', side_effect=[3, 4])
    field = Field(10, 8, 3)
    assert next_move_automatic(field) == (3, 4)


def test_next_move_user(mocker):
    mocker.patch.object(controllers, 'input', return_value='3, 2')
    field = Field(10, 8, 3)
    assert next_move_user(field) == (2, 1)
