from nataliia_romanchuk.homework_8.warior import Warrior, Knight, fight


def test_warrior_mark_carl():
    mark = Warrior()
    carl = Knight()
    assert fight(carl, mark) == False
    assert carl.is_alive == False


def test_chuck_bruce():
    chuck = Warrior()
    bruce = Warrior()
    assert fight(chuck, bruce)
    assert chuck.is_alive
    assert bruce.is_alive == False


def test_dave_carl():
    carl = Knight()
    dave = Warrior()
    assert fight(dave, carl) == False
    assert carl.is_alive
    assert dave.is_alive == False
