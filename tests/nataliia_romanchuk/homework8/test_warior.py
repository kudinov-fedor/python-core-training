from nataliia_romanchuk.homework_8.warior import Warrior, Knight, fight


def test_warrior():
    warrior = Warrior("Alex", body=10, resilience=8, speed=5, arsenal=3)
    assert warrior.base_oppos == [10, 8, 5, 3]
    assert warrior.name == 'Alex'
    assert sum(warrior.base_oppos) == 26


def test_knight():
    knight = Knight(name="John", body=15, resilience=10, speed=5, arsenal=5)
    assert knight.base_oppos == [15, 10, 5, 5]
    assert knight.name == 'John'
    assert knight.base_oppos
    assert sum(knight.base_oppos) == 35


def test_fight_function():
    war1 = Warrior("Gerkules")
    war2 = Knight("Ksena")
    result = fight(unit1=war1, unit2=war2)
    assert result == war2
