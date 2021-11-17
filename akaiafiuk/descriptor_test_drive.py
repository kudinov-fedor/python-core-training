"""
Took a look at a simple tutorial related to python descriptors. And based on it created a descriptor for maximum speed
inside a "Car" object. Positive side of this approach is the fact that now maximum speed value is protected during
object creation and update (only in case when user updates max_speed parameter mentioned in Car class,
_max_speed private attribute still not secured. It is still safer because _max_speed logic is encapsulated inside the
Descriptor and the attribute marked as private)
"""


class Descriptor:

    def __get__(self, instance, objtype=None):
        return instance._max_speed

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("max_speed must be integer")
        if value < 0:
            raise ValueError("max_speed cannot be negative")
        instance._max_speed = value

    def __delete__(self, instance):
        del instance._max_speed


class Car:

    max_speed = Descriptor()

    def __init__(self, make, model, max_speed):
        self.make = make
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "Make: {0}, Model: {1}, Maximum Speed: {2}".format(self.make, self.model, self.max_speed)
