import pytest

from olpopova.homework.homework08.warrior import Warrior, Knight, fight


@pytest.mark.parametrize(['fighter1', 'fighter2', 'expected'],[
    (Warrior, Warrior, True),
    (Warrior, Knight, False)
])
def test_fight(fighter1, fighter2, expected):
    chuck = fighter1()
    bruce = fighter2()
    assert fight(chuck, bruce) is expected
    assert chuck.is_alive is expected
    assert bruce.is_alive is not expected
