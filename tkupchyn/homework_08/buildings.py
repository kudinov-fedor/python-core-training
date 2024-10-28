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

    def corners(self) -> dict:
        ne_corner = [self.south + self.width_ns, self.west + self.width_we]
        nw_corner = [self.south + self.width_ns, self.west]
        se_corner = [self.south, self.west + self.width_we]
        sw_corner = [self.south, self.west]
        return {'north-east': ne_corner,
                'south-east': se_corner,
                'south-west': sw_corner,
                'north-west': nw_corner}

    @property
    def area(self) -> int:
        return self.width_we * self.width_ns

    @property
    def volume(self) -> int:
        return self.area * self.height
