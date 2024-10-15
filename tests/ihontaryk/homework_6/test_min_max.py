import pytest

from ihontaryk.homework_6.min_max import custom_min, custom_max, custom_sorted


@pytest.mark.parametrize('arguments',
                         [(-7, -4, -2, 1, 2, 3, 4, 5, 6, None, -7),
                          (-7, -4, -2, 1, 2, 3, 4, 5, 6, abs, 1),
                          ('a', 'b', 'c', 'd', 'ab', None, 'a'),
                          ])
def test_custom_min(arguments):
    """
    verify custom_min function
    """

    *values, key1, expected_result = arguments
    assert custom_min(*values, key=key1) == expected_result


@pytest.mark.parametrize('arguments',
                         [(-7, -4, -2, 1, 2, 3, 4, 5, 6, None, 6),
                          (-7, -4, -2, 1, 2, 3, 4, 5, 6, abs, -7),
                          ('a', 'b', 'c', 'd', 'ab', None, 'd'),
                          ])
def test_custom_max(arguments):
    """
    verify custom_max function
    """

    *values, key1, expected_result = arguments
    assert custom_max(*values, key=key1) == expected_result


@pytest.mark.parametrize('arguments',
                         [(-7, -4, -2, 1, 6, 2, 3, 4, 5, 8, 7, None, False, [-7, -4, -2, 1, 2, 3, 4, 5, 6, 7, 8]),
                          (-7, -4, -2, 1, 2, 3, 4, 5, 6, None, True, [6, 5, 4, 3, 2, 1, -2, -4, -7]),
                          (-7, -4, -2, 1, 2, 3, 4, 5, 6, abs, False, [1, -2, 2, 3, -4, 4, 5, 6, -7]),
                          (-7, -4, -2, 1, 2, 3, 4, 5, 6, abs, True, [-7, 6, 5, -4, 4, 3, -2, 2, 1]),
('a', 'b', 'b', 'x', 'c', 'd', 'ab', None, True, ['x', 'd', 'c', 'b', 'b', 'ab', 'a']),
('a', 'b', 'b', 'x', 'c', 'd', 'ab', None, False, ['a', 'ab', 'b', 'b', 'c', 'd', 'x']),
                          ])
def test_custom_sorted(arguments):
    """
    verify custom_sorted function
    """

    *values, key1, reverse1, expected_result = arguments

    assert custom_sorted(*values, key=key1, reverse=reverse1) == expected_result
