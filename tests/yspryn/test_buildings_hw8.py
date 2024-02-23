from yspryn.hw8.buildings import Building


def test_buildings():

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)

    assert b.corners() == {'north-east': [4, 4], 'south-east': [1, 4],
                           'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
