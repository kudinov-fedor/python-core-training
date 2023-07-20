class Building:

    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):

        north_west = [self.south + self.width_NS, self.west]
        north_east = [self.south + self.width_NS, self.west + self.width_WE]
        south_west = [self.south, self.west]
        south_east = [self.south, self.west + self.width_WE]
        return {'north-west': north_west,
                'north-east': north_east,
                'south-west': south_west,
                'south-east': south_east}

    def calculated_area(self):
        calculated_area = self.width_WE * self.width_NS
        return calculated_area

    def calculated_volume(self):
        calculated_volume = self.calculated_area() * self.height
        return calculated_volume

    def __repr__(self):
        return f'Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})'



