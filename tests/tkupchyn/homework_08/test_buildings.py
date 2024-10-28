import pytest
from tkupchyn.homework_08.buildings import Building


b1 = Building(1, 2, 2, 3)
b2 = Building(1, 2, 2, 8, 5)


@pytest.mark.parametrize('building, expected_area',
                         (
                                 (b1, 6),
                                 (b2, 16)
                         ))
def test_area(building, expected_area):
    assert building.area == expected_area


@pytest.mark.parametrize('building, expected_volume',
                         (
                                 (b1, 60),
                                 (b2, 80)
                         ))
def test_volume(building, expected_volume):
    assert building.volume == expected_volume


@pytest.mark.parametrize('building, expected_result',
                         (
                                 (b1, {'north-east': [4, 4], 'south-east': [1, 4], 'south-west': [1, 2],
                                       'north-west': [4, 2]}),
                                 (b2, {'north-east': [9, 4], 'south-east': [1, 4], 'south-west': [1, 2],
                                       'north-west': [9, 2]})
                         ))
def test_corners(building, expected_result):
    assert building.corners() == expected_result
