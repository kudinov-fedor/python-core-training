import pytest

import hw8_warior


@pytest.fixture
def chuck():
    return hw8_warior.Warrior()


@pytest.fixture
def bruce():
    return hw8_warior.Warrior()


@pytest.fixture
def carl():
    return hw8_warior.Knight()


@pytest.fixture
def dave():
    return hw8_warior.Warrior()


@pytest.fixture
def mark():
    return hw8_warior.Warrior()


def test_chuck_bruce_fight(chuck, bruce):
    assert hw8_warior.fight(chuck, bruce) == True
    assert chuck.is_alive == True
    assert bruce.is_alive == False


def test_chuck_dave_carl(dave, carl):
    assert hw8_warior.fight(dave, carl) == False
    assert dave.is_alive == False


def test_cart_mark_fight(carl, mark):
    assert hw8_warior.fight(carl, mark) == True
    assert carl.is_alive == True


def test_dave_mark_fight(dave, mark):
    assert hw8_warior.fight(dave, mark) == True
    assert dave.is_alive == True
    assert mark.is_alive == False
