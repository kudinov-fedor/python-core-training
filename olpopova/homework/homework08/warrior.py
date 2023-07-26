
class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def deal_dmg(self, damaged_unit):
        """
        E.g. warrior1.deal_dmg(knight) == 'warrior attack knight'
        """
        return damaged_unit.health - self.attack


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive:
        unit_2.health = unit_1.deal_dmg(unit_2)
        if not unit_2.is_alive:
            break
        unit_1.health = unit_2.deal_dmg(unit_1)
    return unit_1.is_alive
