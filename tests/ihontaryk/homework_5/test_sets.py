import pytest

from ihontaryk.homework_5.sets import remove_min_loop, remove_max_loop


@pytest.mark.parametrize('set1, number1, expected_result',
                         [({'a', 'b'}, 1, {'b'}),
                          ({'a', 'b', 'abc', 'abc2'}, 2, {'abc2', 'b'}),
                          ({1, 2, 3, 4, 5, 6, 7}, 3, {4, 5, 6, 7})
                          ])
def test_remove_min_loop_positive(set1, number1, expected_result):
    """
    verify positive cases for remove_min_oop function
    """
    assert remove_min_loop(set1, number1) == expected_result


@pytest.mark.parametrize('set1, number1, expected_result',
                         [({'a', 'b', 'c'}, 1, {'b', 'a'}),
                          ({'a', 'b', 'abc', 'bcl', 'd'}, 2, {'a', 'abc', 'b'}),
                          ({1, 2, 3, 4, 5, 6, 7}, 3, {1, 2, 3, 4})
                          ])
def test_remove_max_loop_positive(set1, number1, expected_result):
    """
    verify positive cases for remove_max_loop function
    """
    assert remove_max_loop(set1, number1) == expected_result


@pytest.mark.parametrize('set1, number1, error',
                         [({'a', 'b'}, 0, ValueError),
                          ({'a', 'b'}, -1, ValueError),
                          ({'a', 'b'}, 2, ValueError),
                          ({'a', 'b', 1, 2}, 2, TypeError),
                          ({'a', 'b', 1, ('2', '3')}, 2, TypeError)
                          ])
def test_remove_min_loop_negative(set1, number1, error):
    """
    verify raising exceptions for functions remove_min_loop
    """

    with pytest.raises(error):
        remove_min_loop(set1, number1)


@pytest.mark.parametrize('set1, number1, error',
                         [({'a', 'b'}, 0, ValueError),
                          ({'a', 'b'}, -1, ValueError),
                          ({'a', 'b'}, 2, ValueError),
                          ({'a', 'b', 1, 2}, 2, TypeError),
                          ({'a', 'b', 1, ('2', '3')}, 2, TypeError)
                          ])
def test_remove_max_loop_negative(set1, number1, error):
    """
    verify raising exceptions for functions remove_min_max_loop
    """

    with pytest.raises(error):
        remove_max_loop(set1, number1)
