class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
    #{"north-west": [3, 2], "north-east": [3, 4], "south-west": [1, 2], "south-east": [1, 4]}
        north_west = [self.south + self.width_NS, self.west]
        north_east = [self.south + self.width_NS, self.west + self.width_WE]
        south_west = [self.south, self.west]
        south_east = [self.south, self.west + self.width_WE]
        keys = [north_west, north_east, south_west, south_east]
        values = ['north-west', 'north-east', 'south-west', 'south-east']
        return {'north-west': north_west,
                'north-east': north_east,
                'south-west': south_west,
                'south-east': south_east}

    def area(self):
        area_counted = self.width_WE * self.width_NS
        return area_counted

    def volume(self):
        volume_counted = self.area() * self.height
        return volume_counted

    def __repr__(self):
#   "Building({south}, {west}, {width_we}, {width_ns}, {height})"
        return f'{__class__.__name__}({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})'


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {
        "north-east": [4, 4],
        "south-east": [1, 4],
        "south-west": [1, 2],
        "north-west": [4, 2],
    }, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
