from tkupchyn.homework_08.warior import (Warrior, Knight, fight)


def test_is_alive():
    assert Warrior().is_alive


def test_after_duel():
    a, b = Warrior(), Warrior()
    fight(a, b)
    assert a.is_alive
    assert not b.is_alive


def test_duels():
    assert fight(Warrior(), Warrior()) is True
    assert fight(Warrior(), Knight()) is False
    assert fight(Knight(), Knight()) is True
    assert fight(Knight(), Warrior()) is True
