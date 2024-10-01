import pytest


@pytest.mark.parametrize('input1, expected_result',
                         [(['a', 'b', 'c'], [(0, 'a'), (1, 'b'), (2, 'c')]),
                          ('abcd', [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]),
                          (['one', 'two', 'three'], [(0, 'one'), (1, 'two'), (2, 'three')])
                          ])
def test_list_conversion_enumerate(input1, expected_result):
    """
    verify list conversion from enumerate
    """

    assert list(enumerate(input1)) == expected_result


@pytest.mark.parametrize('input1, input2, expected_result',
                         [(['a', 'b', 'c'], [1, 2, 3], [('a', 1), ('b', 2), ('c', 3)]),
                          (['a', 'b', 'c'], [15, 25, 35], [('a', 15), ('b', 25), ('c', 35)]),
                          (['a', 'b', 'c'], ['15', '25', '35'], [('a', '15'), ('b', '25'), ('c', '35')])
                          ])
def test_list_conversion_zip(input1, input2, expected_result):
    """
    verify list conversion from zip
    """

    assert list(zip(input1, input2)) == expected_result


@pytest.mark.parametrize('input1,  expected_result',
                         [({'a': 1, 'b': 2}, [('a', 1), ('b', 2)]),
                          ({'Name': 'Ben', 'Age': 22}, [('Name', 'Ben'), ('Age', 22)])
                          ])
def test_list_conversion_dict_items(input1, expected_result):
    """
    verify list conversion from dictionary items
    """

    assert list(input1.items()) == expected_result
