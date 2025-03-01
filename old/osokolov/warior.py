
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def perform_attack(self, warrior):
        warrior.health -= self.attack

    def take_damage(self, warrior):
        self.health -= warrior.attack


class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7


def fight(warrior_1, warrior_2):
    while True:
        warrior_1.perform_attack(warrior_2)
        if not warrior_2.is_alive:
            break
        else:
            warrior_1.take_damage(warrior_2)
        if not warrior_1.is_alive:
            return False
        else:
            continue
    return True


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
