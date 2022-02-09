from unittest import mock
from unittest.mock import patch
from akaiafiuk.mine_sweeper.controllers import next_move_user, next_move_automatic
from akaiafiuk.mine_sweeper import Field


@patch('akaiafiuk.mine_sweeper.controllers.randint', mock.MagicMock(return_value=2))
def test_next_move_automatic():
    field = Field(10, 8, 3)
    assert next_move_automatic(field) == (2, 2)


@patch('akaiafiuk.mine_sweeper.controllers.input', mock.MagicMock(return_value='2,2'))
def test_next_move_user():
    field = Field(10, 8, 3)
    assert next_move_user(field) == (1, 1)
