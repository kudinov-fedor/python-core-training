class Building:
    def __init__(self, south, west, width_we, width_ns, height=10):
        self.south = south
        self.west = west
        self.width_we = width_we
        self.width_ns = width_ns
        self.height = height

    def __str__(self):
        return f"Building({self.south}, {self.west}, {self.width_we}, {self.width_ns}, {self.height})"

    def corners(self):
        ne_corner = [self.south + self.width_ns, self.west + self.width_we]
        nw_corner = [self.south + self.width_ns, self.west]
        se_corner = [self.south, self.west + self.width_we]
        sw_corner = [self.south, self.west]
        return {'north-east': ne_corner,
                'south-east': se_corner,
                'south-west': sw_corner,
                'north-west': nw_corner}

    def area(self):
        return self.width_we * self.width_ns

    def volume(self):
        return self.width_we * self.width_ns * self.height


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    print(b.corners())
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
