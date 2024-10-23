# Details:  https://py.checkio.org/mission/the-warriors/share/e171c1a99e4e63b4551cfd820252edcd/


class Warrior:

    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def attacks(self, enemy):
        enemy.health -= self.attack

    def _str__(self):
        return f"Warrior ({self.health}, {self.attack}, {self.is_alive})"


class Knight(Warrior):

    attack = 7

    def _str_(self):
        return f"Knight ({self.health}, {self.attack}, {self.is_alive})"


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.attacks(unit_2)
        if unit_2.is_alive:
            unit_2.attacks(unit_1)

    return unit_1.is_alive
