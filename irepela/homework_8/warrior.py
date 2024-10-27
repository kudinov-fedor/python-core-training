# Details:  https://py.checkio.org/mission/the-warriors/share/e171c1a99e4e63b4551cfd820252edcd/


class Warrior:

    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def perform_attack(self, enemy):
        enemy.health -= self.attack

    def __str__(self):
        return f"Warrior ({self.health}, {self.attack}, {self.is_alive})"


class Knight(Warrior):

    attack = 7

    def __str__(self):
        return f"Knight ({self.health}, {self.attack}, {self.is_alive})"


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.perform_attack(unit_2)
        if unit_2.is_alive:
            unit_2.perform_attack(unit_1)

    return unit_1.is_alive
