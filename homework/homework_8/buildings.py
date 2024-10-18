# Details: https://py.checkio.org/mission/building-base/share/3de02090eb5fac4f0da0ced85f9f3f61/


class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        ...


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
