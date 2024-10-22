# Details: https://py.checkio.org/mission/building-base/share/3de02090eb5fac4f0da0ced85f9f3f61/

class Building:

    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        return {
            "north-west": [self.south + self.width_NS, self.west],
            "north-east": [self.south + self.width_NS, self.west + self.width_WE],
            "south-west": [self.south, self.west],
            "south-east": [self.south, self.west + self.width_WE]
        }

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.width_WE * self.width_NS * self.height

    def __str__(self):
        return f"Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})"
