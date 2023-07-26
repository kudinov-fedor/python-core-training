
class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive:
        unit_2.health = unit_2.health - unit_1.attack
        if not unit_2.is_alive:
            break
        unit_1.health = unit_1.health - unit_2.attack
    return unit_1.is_alive
