
class Warrior:
    health = 50
    attack = 5
    is_alive = health > 0


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while True:
        unit_2.__setattr__('health', unit_2.health - unit_1.attack)
        unit_2.__setattr__('is_alive', unit_2.health > 0)
        if not unit_2.is_alive:
            break
        unit_1.__setattr__('health', unit_1.health - unit_2.attack)
        unit_1.__setattr__('is_alive', unit_1.health > 0)
        if not unit_1.is_alive:
            break
    return unit_1.is_alive
