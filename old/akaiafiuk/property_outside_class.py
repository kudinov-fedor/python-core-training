def some_getter(self):
    return self._max_speed


def some_setter(self, value):
    if not isinstance(value, int):
        raise TypeError("max_speed must be integer")
    if value < 0:
        raise ValueError("max_speed cannot be negative")
    self._max_speed = value


def some_deleter(self):
    del self._max_speed


my_property = property(some_getter, some_setter, some_deleter)


class Car:

    max_speed = my_property

    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "Make: {0}, Model: {1}, Maximum Speed: {2}".format(self.make, self.model, self.max_speed)
