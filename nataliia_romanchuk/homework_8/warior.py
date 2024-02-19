class Warrior:
    def __init__(self, name, body=1, resilience=1, speed=1, arsenal=1):
        self.name = name
        self.body = body
        self.resilience = resilience
        self.speed = speed
        self.arsenal = arsenal

    def name(self):
        return self.name

    @property
    def base_oppos(self):
        arts = [self.body, self.resilience, self.speed, self.arsenal]
        return arts

    @property
    def all(self):
        return self.base_oppos


class Knight(Warrior):
    def __init__(self, name, armor=1):
        super().__init__(name)
        self.armor = armor

    def resiliense(self):
        self.resilience += 1

    @property
    def specialties(self):
        return [self.armor]

    @property
    def all(self):
        all = self.base_oppos + self.specialties
        return all


def fight(unit1, unit2):
    unit1_sum = unit1.all
    unit2_sum = unit2.all
    winner = max(unit1_sum, unit2_sum)
    if winner == unit1_sum:
        return unit1
    else:
        return unit2
