import pytest


@pytest.fixture
def some_list() -> list:
    return [1, 2, 3, 'a', 'b', 'c']


def test_len(some_list):
    """
    Easy to find len since start index is included and stop index is not included
    """
    start_index = 2
    stop_index = 5
    assert len(some_list[:stop_index]) == stop_index
    assert len(some_list[start_index:stop_index]) == stop_index - start_index


def test_not_intersected(some_list):
    """Easy to create not intersected list for an index"""
    index = 5
    assert some_list[:index] + some_list[index:] == some_list


def test_step():
    """Basic test for step. Each 'n' element will be cut"""
    original_list = ['h', 'z', 'y', 'e', 'y', 'e', 'l', 'y', 'e', 'l', 'y', 'e', 'o']
    sliced = original_list[::3]
    assert sliced == ['h', 'e', 'l', 'l', 'o']


def test_reverse_list():
    """Can reverse a list using step '-1'"""
    original_list = [1, 2, 3, 4, 5]
    reversed_list = original_list[::-1]
    assert reversed_list == [5, 4, 3, 2, 1]


def test_negative_step():
    """Reverse and cut each 'n' element"""
    original_list = [1, 2, 3, 4, 5, 6]
    sliced = original_list[3: 1: -2]  # start at 3(included), stop at 1(not included), step is -2
    assert sliced == [4]


def test_named_slice():
    """Can create named slices for future reuse with containers with the same pattern"""
    patterned_list_1 = [1, 2, 3, 'a', 'b', 'c']
    patterned_list_2 = [10, 20, 30, 'x', 'y', 'z']
    numbers = slice(3)
    letters = slice(3, 6)
    assert patterned_list_1[numbers] == [1, 2, 3]
    assert patterned_list_2[numbers] == [10, 20, 30]
    assert patterned_list_1[letters] == ['a', 'b', 'c']
    assert patterned_list_2[letters] == ['x', 'y', 'z']


def test_convert_slices():
    """Can replace slices in the list. In this test each 2nd element starting from 0 is converted to str"""
    ints = [1, 2, 3, 4, 5, 6]
    ints[::2] = [str(i) for i in ints[::2]]
    assert all([isinstance(i, str) for i in ints[::2]])
    assert all([isinstance(i, int) for i in ints[1::2]])


def test_insert_slices():
    """Can insert slices in the list. Original elements will be replaced."""
    ints = [1, 2, 3, 4, 5, 6]
    chars = ['a', 'b', 'c', 'd', 'e']
    ints[1:5] = chars[0:2]
    assert ints == [1, 'a', 'b', 6]


def test_remove_slices():
    """Can remove slices. In this example elements 3-5 will be removed"""
    ints = [0, 1, 2, 3, 4, 5]
    ints = ints[:3]
    assert ints == [0, 1, 2]
