class Building:
    def __init__(self, south, west, width_we, width_ns, height=10):
        self.south = south
        self.west = west
        self.width_we = width_we
        self.width_ns = width_ns
        self.height = height

    def corners(self):
        my_corners = {"north-west": [self.south + self.width_ns, self.west],
                      "north-east": [self.south + self.width_ns, self.west + self.width_we],
                      "south-west": [self.south, self.west],
                      "south-east": [self.south, self.west + self.width_we]}
        return my_corners

    def area(self):
        return self.width_we * self.width_ns

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return f"Building({self.south}, {self.west}, {self.width_we}, {self.width_ns}, {self.height})"
