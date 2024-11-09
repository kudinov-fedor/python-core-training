import pytest

from ihontaryk.homework_6.unpack import unpack_while_loop, unpack_recursive, unpack_while_loop_gen, unpack_recursive_gen


@pytest.mark.parametrize('arguments, expected_result',
                         [([123, '234', ['adc', None]],
                           [123, '234', 'adc', None]),
                          ([123, {"sdf": True, "bb": 44}],
                           [123, 'sdf', True, 'bb', 44]),
                          ([123, {(1, 2, 3): 'abc'}],
                           [123, 1, 2, 3, 'abc'])
                          ])
def test_unpack_while_loop(arguments, expected_result):
    """
    verify unpack_while_loop function
    """

    assert unpack_while_loop(arguments) == expected_result


@pytest.mark.parametrize('arguments, expected_result',
                         [([123, '234', ['adc', None]],
                           [123, '234', 'adc', None]),
                          ([123, {"sdf": True, "bb": 44}],
                           [123, 'sdf', True, 'bb', 44]),
                          ([123, {(1, 2, 3): 'abc'}],
                           [123, 1, 2, 3, 'abc'])
                          ])
def test_unpack_recursive(arguments, expected_result):
    """
    verify unpack_recursive function
    """

    assert unpack_recursive(arguments) == expected_result


@pytest.mark.parametrize('arguments, expected_result',
                         [([123, '234', ['adc', None]],
                           [123, '234', 'adc', None]),
                          ([123, {"sdf": True, "bb": 44}],
                           [123, 'sdf', True, 'bb', 44]),
                          ([123, {(1, 2, 3): 'abc'}],
                           [123, 1, 2, 3, 'abc'])
                          ])
def test_unpack_while_loop_gen(arguments, expected_result):
    """
    verify unpack_while_loop_gen function
    """

    assert list(unpack_while_loop_gen(arguments)) == expected_result


@pytest.mark.parametrize('arguments, expected_result',
                         [([123, '234', ['adc', None]],
                           [123, '234', 'adc', None]),
                          ([123, {"sdf": True, "bb": 44}],
                           [123, 'sdf', True, 'bb', 44]),
                          ([123, {(1, 2, 3): 'abc'}],
                           [123, 1, 2, 3, 'abc'])
                          ])
def test_unpack_recursive_gen(arguments, expected_result):
    """
    verify unpack_recursive_gen function
    """

    assert list(unpack_recursive_gen(arguments)) == expected_result
