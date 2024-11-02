# Details: https://py.checkio.org/mission/building-base/share/3de02090eb5fac4f0da0ced85f9f3f61/


class Building:
    def __init__(self, south, west, width_we, width_ns, height=10):
        self.south = south
        self.west = west
        self.width_we = width_we
        self.width_ns = width_ns
        self.height = height

    def __str__(self):
        return f"Building({self.south}, {self.west}, {self.width_we}, {self.width_ns}, {self.height})"

    @property
    def ne_corner(self) -> list:
        return [self.south + self.width_ns, self.west + self.width_we]

    @property
    def nw_corner(self) -> list:
        return [self.south + self.width_ns, self.west]

    @property
    def se_corner(self) -> list:
        return [self.south, self.west + self.width_we]

    @property
    def sw_corner(self) -> list:
        return [self.south, self.west]

    def corners(self) -> dict:
        return {'north-east': self.ne_corner,
                'south-east': self.se_corner,
                'south-west': self.sw_corner,
                'north-west': self.nw_corner}

    @property
    def area(self) -> int:
        return self.width_we * self.width_ns

    @property
    def volume(self) -> int:
        return self.area * self.height
