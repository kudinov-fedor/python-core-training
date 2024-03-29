"""https://py.checkio.org/en/mission/the-warriors/"""


class Warrior:
    HEALTH = 50

    def __init__(self, attack: int = 5):
        self.attack = attack

    @property
    def is_alive(self):
        return self.HEALTH > 0

    def perform_attack(self, attacked_unit: "Warrior"):
        dmg = self.attack
        attacked_unit.take_damage(dmg)

    def take_damage(self, dmg_took: int):
        self.HEALTH -= dmg_took


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


def fight(unit_1: Warrior, unit_2: Warrior):
    while unit_1.is_alive:
        unit_1.perform_attack(unit_2)
        if not unit_2.is_alive:
            break
        unit_2.perform_attack(unit_1)
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    # There is explicit verification that result is True/False, I believe it's redundant
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
