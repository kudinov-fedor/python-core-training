from irepela.homework_8.buildings import Building


def test_first_building():
    b = Building(1, 2, 2, 3)
    assert b.corners() == {'north-east': [4, 4], 'south-east': [1, 4], 'south-west': [1, 2], 'north-west': [4, 2]}
    assert b.area() == 6
    assert b.volume() == 60
    assert str(b) == "Building(1, 2, 2, 3, 10)"


def test_second_building():
    b = Building(1, 2, 2, 3, 5)
    assert b.area() == 6
    assert b.volume() == 30
    assert str(b) == "Building(1, 2, 2, 3, 5)"
