class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def perform_attack(self, warrior: "Warrior"):
        warrior.receive_dmg(self.attack)

    def receive_dmg(self, damage: int):
        self.health = max(0, self.health - damage)


class Knight(Warrior):
    attack = 7


def fight(unit_1: Warrior, unit_2: Warrior):
    while unit_1.is_alive:
        unit_1.perform_attack(unit_2)
        if not unit_2.is_alive:
            break
        unit_2.perform_attack(unit_1)
    return unit_1.is_alive