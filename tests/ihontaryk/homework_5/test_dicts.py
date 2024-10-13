import pytest

from ihontaryk.homework_5.dicts import *

data1 = [{'name': 'Hats', 'availability': [{'size': 'S', 'color': 'white', 'price': 400},
                                           {'size': 'M', 'color': 'pink', 'price': 100},
                                           {'size': 'S', 'color': 'black', 'price': 300},
                                           {'size': 'L', 'color': 'yellow', 'price': 200},
                                           {'size': 'M', 'color': 'yellow', 'price': 400}]}]

data2 = [{'name': 'Pajamas', 'availability': [{'size': 'S', 'color': 'blue', 'price': 200},
                                              {'size': 'M', 'color': 'blue', 'price': 100},
                                              {'size': 'L', 'color': 'black', 'price': 200},
                                              {'size': 'S', 'color': 'yellow', 'price': 200},
                                              {'size': 'L', 'color': 'gray', 'price': 500}]}]


@pytest.mark.parametrize('data, expected_result',
                         [(data1, ({'S': 2}, {'M': 2}, {'L': 1})),
                          (data2, ({'S': 2}, {'M': 1}, {'L': 2}))
                          ])
def test_group_by_size(data, expected_result):
    """
    verify group_by_size function
    """
    assert group_by_size(data) == expected_result


@pytest.mark.parametrize('data, expected_result',
                         [(data1, (('white', 1), ('pink', 1), ('black', 1), ('yellow', 2))),
                          (data2, (('blue', 2), ('black', 1), ('yellow', 1), ('gray', 1)))
                          ])
def test_group_by_color(data, expected_result):
    """
    verify group_by_color function
    """
    assert group_by_color(data) == expected_result


@pytest.mark.parametrize('data, expected_result',
                         [(data1, [(100, 1), (200, 1), (300, 1), (400, 2)]),
                          (data2, [(100, 1), (200, 3), (500, 1)])
                          ])
def test_group_by_price(data, expected_result):
    """
    verify group_by_price function
    """
    assert sorted(group_by_price(data)) == expected_result


@pytest.mark.parametrize('data1, data2, name, color, expected_result',
                         [(data1, data2, 'Hats', 'yellow', ({'size': 'L', 'color': 'yellow', 'price': 200},
                                                            {'size': 'M', 'color': 'yellow', 'price': 400})),
                          (data1, data2, 'Pajamas', 'gray', ({'size': 'L', 'color': 'gray', 'price': 500},))
                          ])
def test_select_by_name_and_color(data1, data2, name, color, expected_result):
    """
    verify select_by_name_and_color function
    """
    data = data1 + data2
    assert select_by_name_and_color(data, name, color) == expected_result
