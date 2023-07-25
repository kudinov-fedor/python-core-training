class Building:

    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.x1 = south
        self.y1 = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.y2 = self.y1 + self.width_NS
        self.x2 = self.x1 + self.width_WE
        self.height = height

    def corners(self):
        return {
            'south-west': (self.x1, self.y1),
            'north-west': (self.x2, self.y1),
            'north-east': (self.x2, self.y2),
            'south-east': (self.x1, self.y2)
        }

    def area(self):
        return self.width_NS * self.width_WE

    def volume(self):
        return Building.area(self) * self.height

    def __repr__(self):
        return f'{Building.__name__}{self.x1, self.y1, self.width_WE, self.width_NS, self.height}'
