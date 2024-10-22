from irepela.homework_8.warrior import Warrior, Knight, fight


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()


def test_fight():
    assert fight(chuck, bruce) is True
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert fight(dave, carl) is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
