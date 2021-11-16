"""
Took a look at a simple tutorial related to python descriptors. And based on it created a descriptor for maximum speed
inside a "Car" object. Positive side of this approach is the fact that now maximum speed value is protected during
object creation and update
"""


class Descriptor:
    def __init__(self):
        self._max_speed = 0

    def __get__(self, obj, objtype=None):
        return self._max_speed

    def __set__(self, obj, value):
        if isinstance(value, int):
            if value > 0:
                self._max_speed = value
            else:
                raise ValueError("max_speed cannot be negative")
        else:
            raise TypeError("max_speed must be integer")

    def __delete__(self, obj):
        del self._max_speed


class Car:
    max_speed = Descriptor()

    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed
        if self.max_speed < 0:
            raise ValueError("Max speed cannot be negative")

    def __str__(self):
        return "Make: {0}, Model: {1}, Maximum Speed: {2}".format(self.make, self.model, self.max_speed)
