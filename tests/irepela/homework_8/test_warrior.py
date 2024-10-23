from irepela.homework_8.warrior import Warrior, Knight, fight


def test_fight():
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) is True
    assert chuck.is_alive
    assert not bruce.is_alive
    assert fight(dave, carl) is False
    assert carl.is_alive
    assert not dave.is_alive
    assert fight(carl, mark) is False
    assert not carl.is_alive
