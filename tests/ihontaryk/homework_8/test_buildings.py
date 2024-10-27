import pytest
from ihontaryk.homework_8.buildings import Building


@pytest.mark.parametrize('arguments, expected_result',
                         [((1, 2.5, 4.2, 1.25, 101),
                           {'corners_coordinates': {'north-east': [2.25, 6.7], 'south-east': [1, 6.7], 'south-west': [1, 2.5], 'north-west': [2.25, 2.5]}, 'area': 5.25, 'volume': 530.25}),
                          ((0, 0, 10.5, 2.546),
                           {'corners_coordinates': {'north-east': [2.546, 10.5], 'south-east': [0, 10.5], 'south-west': [0, 0], 'north-west': [2.546, 0]}, 'area': 26.73, 'volume': 267.30})
                          ])
def test_show_building(arguments, expected_result):
    """
    verify show_building function
    """
    south, west, width_WE, width_NS, *height = arguments
    b = Building(south, west, width_WE, width_NS, *height)

    assert b.show_building() == expected_result
