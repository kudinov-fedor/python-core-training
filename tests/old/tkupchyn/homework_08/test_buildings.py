import pytest
from tkupchyn.homework_08.buildings import Building


@pytest.mark.parametrize('building_params, expected_area',
                         [
                             ([1, 2, 2, 3], 6),
                             ([1, 2, 2, 8, 5], 16)
                         ])
def test_area(building_params, expected_area):
    building = Building(*building_params)
    assert building.area == expected_area


@pytest.mark.parametrize('building_params, expected_volume',
                         [
                             ([1, 2, 2, 3], 60),
                             ([1, 2, 2, 8, 5], 80)
                         ])
def test_volume(building_params, expected_volume):
    building = Building(*building_params)
    assert building.volume == expected_volume


@pytest.mark.parametrize('building_params, expected_result',
                         [
                             ([1, 2, 2, 3],
                              {'north-east': [4, 4], 'south-east': [1, 4], 'south-west': [1, 2],
                               'north-west': [4, 2]}),

                             ([1, 2, 2, 8, 5],
                              {'north-east': [9, 4], 'south-east': [1, 4], 'south-west': [1, 2],
                               'north-west': [9, 2]})
                         ])
def test_corners(building_params, expected_result):
    building = Building(*building_params)
    assert building.corners() == expected_result
