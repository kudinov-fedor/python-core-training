import pytest
from ppyze import homework_scope_decorators as hsd
from homework.homework_7 import sorting


@pytest.mark.parametrize('var, expected', [
    (12, 12),
    (14, 14),
    ('test', 'test')
])
def test_change_global_value(var, expected):
    hsd.global_value = 11
    assert hsd.change_global_value(var) == expected
    assert hsd.global_value == expected


@pytest.mark.parametrize('expected,', [
    11,
])
def test_get_global_value(expected):
    hsd.global_value = 11
    assert hsd.get_global_value() == expected


@hsd.add_retry_function
def test_unstable_function():
    assert hsd.unstable_function() >= 0.5


@pytest.mark.parametrize('unsorted, reverse, output', [
    ([8, 6, 5, 4, 3, 2], False, [2, 3, 4, 5, 6, 8]),
    ([100, 90, 40, 80], False, [40, 80, 90, 100])
])
@hsd.time_it
def test_bubble_sort(unsorted, reverse, output):
    assert sorting.bubble_sort(unsorted, reverse) == output


@pytest.mark.parametrize('unsorted, reverse, output', [
    ([8, 6, 5, 4, 3, 2], False, [2, 3, 4, 5, 6, 8]),
    ([100, 90, 40, 80], False, [40, 80, 90, 100])
])
@hsd.time_it
def test_gnome_sort(unsorted, reverse, output):
    assert sorting.gnome_sort(unsorted, reverse) == output


@pytest.mark.parametrize('unsorted, reverse, output', [
    ([8, 6, 5, 4, 3, 2], False, [2, 3, 4, 5, 6, 8]),
    ([100, 90, 40, 80], False, [40, 80, 90, 100])
])
@hsd.time_it
def test_insert_sort(unsorted, reverse, output):
    assert sorting.insert_sort(unsorted, reverse) == output


@pytest.mark.parametrize('unsorted, reverse, output', [
    ([8, 6, 5, 4, 3, 2], False, [2, 3, 4, 5, 6, 8]),
    ([100, 90, 40, 80], False, [40, 80, 90, 100])
])
@hsd.time_it
def test_select_sort(unsorted, reverse, output):
    assert sorting.select_sort(unsorted, reverse) == output


@pytest.mark.parametrize('num, output', [
    (0, 0),
    (1, 1),
    (2, 3),
    (3, 6),
    (10, 55)
])
def test_fibo(num, output):
    assert hsd.fibo(num) == output

