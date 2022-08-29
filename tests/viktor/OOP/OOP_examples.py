
# Vehicle (завод, не имеет отношения к авто которые строит
# auto (авто друг о друге ничего не знают
# но знают завод на котором были изготовлены
# авто не знает ничего о себе о brake and drive он может спросить об этом у завода
#
#
# auto = __new__()
# __init__(auto, color = red, door = 4, tires = 4, AC = ON)
import  this

class Vehicle(object):
    """docstring"""
    color = 'black'
    def __init__(car, light, doors, tires):
        """Constructor"""
        color = light
        # car.color = color
        car.doors = doors
        car.tires = tires

    def get_color(vehicle):
        print(vehicle.color)

    def brake(self):
        """
        Stop the car
        """
        return "Braking"

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving!"


car1 = Vehicle('green', 6, 4)
car2 = Vehicle('blue', 2, 3)
# print(car1.color, car2.color)
car1.get_color()   # which color of auto

Vehicle.get_color(car1)
print(type(car1))
type(car1).get_color(car1)

# class Colored:
#     color = 'blue'

Vehicle.color = 'blue'
car1.get_color()   # which color of auto
car1.color = "red"
car1.get_color()