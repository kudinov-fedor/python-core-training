from nataliia_romanchuk.homework_8.warior import Warrior, Knight, fight


def test_warrior_mark_carl():
    carl = Knight()
    mark = Warrior()
    assert fight(carl, mark)
    assert carl.is_alive


def test_chuck_bruce():
    chuck = Warrior()
    bruce = Warrior()
    assert fight(chuck, bruce)
    assert chuck.is_alive
    assert not bruce.is_alive


def test_dave_carl():
    carl = Knight()
    dave = Warrior()
    assert not fight(dave, carl)
    assert carl.is_alive
    assert not dave.is_alive
