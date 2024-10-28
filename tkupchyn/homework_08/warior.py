# Details:  https://py.checkio.org/mission/the-warriors/share/e171c1a99e4e63b4551cfd820252edcd/


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack_damage = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack_damage = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack_damage
        if not unit_2.is_alive:
            return True
        else:
            unit_1.health -= unit_2.attack_damage
    return False



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    # print(chuck.is_alive)
    # print(fight(chuck, bruce))
    # print(chuck.is_alive)
    # print(bruce.is_alive)
    # print(fight(dave, carl))
    assert fight(chuck, bruce)
    assert fight(dave, carl) == False
    assert chuck.is_alive
    assert bruce.is_alive == False
    assert carl.is_alive
    assert not dave.is_alive
    assert not fight(carl, mark)
    assert not carl.is_alive