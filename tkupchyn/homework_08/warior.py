# Details:  https://py.checkio.org/mission/the-warriors/share/e171c1a99e4e63b4551cfd820252edcd/


class Warrior:

    health = 50
    attack_damage = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def attack(self, enemy):
        enemy.health -= self.attack_damage


class Knight(Warrior):
    attack_damage = 7


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    """
    Returns the result of fight between two units. True if the first unit wins, else False
    """

    while unit_1.is_alive and unit_2.is_alive:
        unit_1.attack(unit_2)
        if not unit_2.is_alive:
            break
        else:
            unit_2.attack(unit_1)

    return unit_1.is_alive
