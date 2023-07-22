from mizo.task_min_max import minimum_custom, maximum_custom, \
    my_sorted


def test_min_assertions():
    assert minimum_custom(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7


def test_max_assertions():
    assert maximum_custom(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6


def test_absolute_value():
    assert minimum_custom(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1


def test_sorted():
    assert my_sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
