import pytest
import hw8_buildings


@pytest.fixture
def building2():
    return hw8_buildings.Building(1, 2, 2, 3, 8)


def test_building_1():
    b = hw8_buildings.Building(1, 2, 2, 3)
    assert b.corners() == {'north-east': [4, 4], 'south-east': [1, 4],
                           'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"


def test_corners_building_2(building2):
    build_2_corners = building2.corners()
    assert build_2_corners == {'north-east': [4, 4], 'south-east': [1, 4],
                               'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"


def test_volume_building_2(building2):
    build_2_volume = building2.volume()
    assert build_2_volume == 48, "Volume"


def test_area_building_2(building2):
    build_2_area = building2.area()
    assert build_2_area == 6, "Area"


def test_string_inter_build_2(building2):
    build_info = str(building2)
    assert build_info == "Building(1, 2, 2, 3, 8)", "String"
