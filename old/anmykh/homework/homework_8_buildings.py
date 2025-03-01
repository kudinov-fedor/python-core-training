class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.north = south + width_NS
        self.west = west
        self.east = west + width_WE
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {'north-east': [self.north, self.east], 'south-east': [self.south, self.east],
                'south-west': [self.south, self.west], 'north-west': [self.north, self.west]}

    def area(self):
        return abs(self.north - self.south) * abs(self.west - self.east)

    def volume(self):
        return self.area() * self.height

    def __str__(self):
        return f"Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})"
