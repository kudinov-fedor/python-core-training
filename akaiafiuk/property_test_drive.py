class Car:

    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "Make: {0}, Model: {1}, Maximum Speed: {2}".format(self.make, self.model, self.max_speed)

    @property
    def max_speed(self):
        return self._max_speed

    @max_speed.setter
    def max_speed(self, value):
        if not isinstance(value, int):
            raise TypeError("max_speed must be integer")
        if value < 0:
            raise ValueError("max_speed cannot be negative")
        self._max_speed = value

    @max_speed.deleter
    def max_speed(self):
        del self._max_speed
