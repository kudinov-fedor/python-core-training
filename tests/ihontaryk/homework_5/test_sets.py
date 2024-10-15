import pytest

from ihontaryk.homework_5.sets import remove_min_max_loop


@pytest.mark.parametrize('set1, number1, expected_result',
                         [({'a', 'b'}, 1, set()),
                          ({'a', 'b', 'c'}, 1, {'b'}),
                          ({1, 2, 3, 4, 5, 6, 7}, 3, {4}),
                          ({'a', 'b', 'abc', 'abc2'}, 2, set()),
                          ({'a', 'b', 'abc', 'bcl', 'd'}, 2, {'b'})
                          ])
def test_remove_min_max_loop_positive(set1, number1, expected_result):
    """
    verify positive cases for remove_min_max_loop function
    """
    assert remove_min_max_loop(set1, number1) == expected_result


@pytest.mark.parametrize('set1, number1, error',
                         [({'a', 'b'}, 0, ValueError),
                          ({'a', 'b'}, -1, ValueError),
                          ({'a', 'b'}, 2, ValueError),
                          ({'a', 'b', 1, 2}, 2, TypeError),
                          ({'a', 'b', 1, ('2', '3')}, 2, TypeError)
                          ])
def test_remove_min_max_loop_negative(set1, number1, error):
    """
    verify raising exceptions for functions remove_min_max_loop
    """

    with pytest.raises(error):
        remove_min_max_loop(set1, number1)
