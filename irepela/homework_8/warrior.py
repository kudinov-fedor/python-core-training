# Details:  https://py.checkio.org/mission/the-warriors/share/e171c1a99e4e63b4551cfd820252edcd/


class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True

    def hit(self, damage):
        if self.health > 0:
            self.health = self.health - damage
        else:
            self.is_alive = False

    def _str__(self):
        return f"Warrior ({self.health}, {self.attack}, {self.is_alive})"


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7

    def _str__(self):
        return f"Knight ({self.health}, {self.attack}, {self.is_alive})"


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    while unit_1.is_alive and unit_2.is_alive:
        # unit 2 is hit first
        if unit_1.is_alive:
            unit_2.hit(unit_1.attack)
        if unit_2.is_alive:
            unit_1.hit(unit_2.attack)

    return unit_1.is_alive
