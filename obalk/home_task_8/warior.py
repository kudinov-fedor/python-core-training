"""https://py.checkio.org/en/mission/the-warriors/"""


class Warrior:
    def __init__(self, attack: int = 5):
        self.health = 50
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


def fight(unit_1: Warrior, unit_2: Warrior):
    while True:
        unit_2.health = max(0, unit_2.health - unit_1.attack)
        if unit_2.is_alive:
            unit_1.health = max(0, unit_1.health - unit_2.attack)
            if not unit_1.is_alive:
                return False
        else:
            return True


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
