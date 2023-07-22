from mizo.task_min_max import test_minimum_custom, test_minimum_absolute_custom, test_maximum_custom, \
    test_sorted_function


def test_min_assertions():
    assert test_minimum_custom(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7


def test_max_assertions():
    assert test_maximum_custom(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6


def test_absolute_value():
    assert test_minimum_absolute_custom(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1


def test_sorted():
    assert test_sorted_function(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=False) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
