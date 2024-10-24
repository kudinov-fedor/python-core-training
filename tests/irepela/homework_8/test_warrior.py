from irepela.homework_8.warrior import Warrior, Knight, fight


def test_fight():
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert str(chuck) == "Warrior (50, 5, True)"
    assert str(bruce) == "Warrior (50, 5, True)"
    assert fight(chuck, bruce) is True
    assert chuck.is_alive
    assert not bruce.is_alive
    assert str(chuck) == "Warrior (5, 5, True)"
    assert str(bruce) == "Warrior (0, 5, False)"

    assert str(dave) == "Warrior (50, 5, True)"
    assert str(carl) == "Knight (50, 7, True)"
    assert fight(dave, carl) is False
    assert carl.is_alive
    assert not dave.is_alive
    assert str(dave) == "Warrior (-6, 5, False)"
    assert str(carl) == "Knight (10, 7, True)"

    assert str(carl) == "Knight (10, 7, True)"
    assert str(mark) == "Warrior (50, 5, True)"
    assert fight(carl, mark) is False
    assert not carl.is_alive
    assert str(carl) == "Knight (0, 7, False)"
    assert str(mark) == "Warrior (36, 5, True)"
