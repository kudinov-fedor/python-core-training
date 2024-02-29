import pytest
from anmykh.homework.homework_8_buildings import Building


def test_buildings_corners():
    b = Building(1, 2, 2, 3)
    assert b.corners() == {'north-east': [4, 4], 'south-east': [1, 4],
                           'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"


def test_buildings_volume():
    building = Building(0, 6, 4, 2)
    assert building.volume() == 80


def test_buildings_area():
    building = Building(10, 15, 9, 5)
    assert building.area() == 45


def test_buildings_str():
    building = Building(3, 6, 4, 2, 10)
    assert building.__str__() == "Building(3, 6, 4, 2, 10)", "String"
