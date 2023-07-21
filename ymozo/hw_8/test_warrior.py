import hw8_warior

chuck = hw8_warior.Warrior()
bruce = hw8_warior.Warrior()
carl = hw8_warior.Knight()
dave = hw8_warior.Warrior()
mark = hw8_warior.Warrior()


def test_chuck_bruce_fight():
    assert hw8_warior.fight(chuck, bruce) == True


def test_chuck_dave_carl():
    assert hw8_warior.fight(dave, carl) == False


def test_cart_mark_fight():
    assert hw8_warior.fight(carl, mark) == False


def test_chuck_is_alive():
    assert chuck.is_alive == True


def test_bruce_is_alive():
    assert bruce.is_alive == False


def test_carl_is_alive():
    assert carl.is_alive == True


def test_dave_is_alive():
    assert dave.is_alive == False


def test_carl_is_alive():
    assert carl.is_alive == False
