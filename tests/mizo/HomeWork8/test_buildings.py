from mizo.task_buildings import Building


def json_dict(d):
    return dict((k, list(v)) for k, v in d.items())


b = Building(1, 2, 2, 3)
b2 = Building(1, 2, 2, 3, 5)


def test_attributes():
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.calculated_area() == 6, "Area"
    assert b.calculated_volume() == 60, "Volume"
    assert b2.calculated_volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
