
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def receive_dmg(self, dmg: int):
        self.health = self.health - dmg

    def attack_enemy(self, enemy: "Warrior"):
        enemy.receive_dmg(self.attack)

class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7


def fight(unit_1: "Warrior", unit_2: "Warrior"):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.attack_enemy(unit_2)
        if unit_2.is_alive:
            unit_2.attack_enemy(unit_1)
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
