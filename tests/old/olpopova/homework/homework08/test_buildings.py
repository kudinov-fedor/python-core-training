from olpopova.homework.homework08.buildings import Building


def test_buildings():
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(5, 7, 8, 10, 30)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [13, 17], 'south-east': [5, 17],
                                      'south-west': [5, 7], 'north-west': [13, 7]}, "Corners"
    assert b.area() == 80, "Area"
    assert b.volume() == 2400, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(5, 7, 8, 10, 30)", "Values are not equal"
