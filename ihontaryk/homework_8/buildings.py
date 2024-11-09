class Building:
    def __init__(self, south, west, width_we, width_ns, height=10):
        self.south = south
        self.west = west
        self.width_we = width_we
        self.width_ns = width_ns
        self.height = height

    @property
    def east(self):
        return self.west + self.width_we

    @property
    def north(self):
        return self.south + self.width_ns

    @property
    def corners_coordinates(self):
        """
        Returns a dictionary with the coordinates of the building corners.
        """

        return {'north-east': [self.north, self.east],
                'south-east': [self.south, self.east],
                'south-west': [self.south, self.west],
                'north-west': [self.north, self.west]}

    @property
    def area(self):
        """
        Returns the area of the building.
        """

        return round(self.width_we * self.width_ns, 2)

    @property
    def volume(self):
        """
        Returns the volume of the building.
        """

        return round((self.area * self.height), 2)

    def __repr__(self):
        """
        This is a string representation of the Building.
        This method is used for 'print' or 'str' conversion.
        """

        return f'Building({self.south}, {self.west}, {self.width_we}, {self.width_ns}, {self.height})'

    def show_building(self) -> dict:
        return {'corners_coordinates': self.corners_coordinates, 'area': self.area, 'volume': self.volume}


if __name__ == '__main__':
    b = Building(0, 0, 10.5, 2.546)
    print(b.show_building())
