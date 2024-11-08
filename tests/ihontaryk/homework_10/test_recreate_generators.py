import pytest

from ihontaryk.homework_10.recreate_generators import (custom_zip, custom_enumerate,
                                                       custom_filter, custom_map, filter_int)


@pytest.mark.parametrize('test_iterable1, test_iterable2, test_iterable3, expected_result',
                         [(["a", "b", "c"], ["x", "y", "z"], [1, 2, 4],
                           [("a", "x", 1), ("b", "y", 2), ("c", "z", 4)]),
                          (["a", "b", "c"], [0, 3, 6], ["x", "y", "z"],
                           [("a", 0, "x"), ("b", 3, "y"), ("c", 6, "z")])
                          ])
def test_custom_zip(test_iterable1, test_iterable2, test_iterable3, expected_result):
    """
    verify custom_zip function
    """

    generator = custom_zip(test_iterable1, test_iterable2, test_iterable3)
    assert list(generator) == expected_result


@pytest.mark.parametrize('test_iterable, start, expected_result',
                         [(["a", "b", "c"], 0,
                           [(0, "a"), (1, "b"), (2, "c")]),
                          (["a", "b", "c"], 2,
                           [(2, "a"), (3, "b"), (4, "c")]),
                          ])
def test_custom_enumerate(test_iterable, start, expected_result):
    """
    verify custom_enumerate function
    """

    generator = custom_enumerate(test_iterable, start=start)
    assert list(generator) == expected_result


@pytest.mark.parametrize('test_iterable, key, expected_result',
                         [([0, 1, 2, 0, 2, 3], None,
                           [1, 2, 2, 3]),
                          ([0.5, 1, 2.4, 0.8, 2, 3, 9], filter_int,
                           [1, 2, 3, 9]),
                          ])
def test_custom_filter(test_iterable, key, expected_result):
    """
    verify custom_filter function
    """

    generator = custom_filter(key, test_iterable)
    assert list(generator) == expected_result


@pytest.mark.parametrize('test_iterable, func, expected_result',
                         [([0, 1, 2, 0, 2, 3], str,
                           ['0', '1', '2', '0', '2', '3']),
                          ([0, 1, 2, 0, 2, 3], bool,
                           [False, True, True, False, True, True]),
                          ])
def test_custom_map(test_iterable, func, expected_result):
    """
    verify custom_map function
    """

    generator = custom_map(func, test_iterable)
    assert list(generator) == expected_result
