
class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def perform_attack(self, warrior: "Warrior"):
        warrior.received_damage(self.attack)

    def received_damage(self, damage):
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
