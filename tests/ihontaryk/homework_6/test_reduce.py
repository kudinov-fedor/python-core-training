from operator import add, mul

import pytest

from ihontaryk.homework_6.reduce import custom_reduce


@pytest.mark.parametrize('arguments',
                         [(-7, -4, -2, 1, 2, 3, 4, 5, 6, add, 0, 8),
                          (-7, -4, -2, 1, 2, 3, 4, 5, 6, mul, 1, -40320),
                          ('a', 'b', 'c', 'd', 'ab', add, '', 'abcdab'),
                          ])
def test_custom_reduce(arguments):
    """
    verify custom_reduce function
    """

    *values, key1, default1, expected_result = arguments
    assert custom_reduce(*values, key=key1, default=default1) == expected_result
