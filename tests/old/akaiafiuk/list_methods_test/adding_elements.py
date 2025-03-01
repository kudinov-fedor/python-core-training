import pytest


@pytest.fixture
def some_list() -> list:
    return [1, 2, 3, 'a', 'b', 'c']


@pytest.mark.parametrize('append_with_item', [
    1,
    'a',
    'new_item',
    [1, 2, 3, 4],
])
def test_append_positive(some_list, append_with_item):
    """Append adds an element to the end of the list"""
    some_list.append(append_with_item)
    assert some_list == [1, 2, 3, 'a', 'b', 'c', append_with_item]  # Iterable is added as a single item


def test_extend_positive(some_list):
    """Extend extends the list with items from iterable"""
    some_list.extend("item")
    assert some_list[-4:] == ['i', 't', 'e', 'm']


@pytest.mark.parametrize('non_iterable', [
    1,
    True,
    3.14
])
def test_extend_negative(some_list, non_iterable):
    """Cannot use extend if not an iterable"""
    with pytest.raises(TypeError, match='object is not iterable'):
        some_list.extend(non_iterable)


@pytest.mark.parametrize('index_to_put, index_stored_to', [
    (0, 0),                 # If insert as a first element, the item will be stored as a first element
    (3, 3),                 # Insert at index 3, stored at index 3
    (-1, -2),               # Insert before the last element, stored before the last element
])
def test_insert_positive(some_list, index_to_put, index_stored_to):
    """Insert an element in the position before the mentioned index"""
    old_value = some_list[index_to_put]
    some_list.insert(index_to_put, 'added_value')
    assert some_list[index_stored_to] == 'added_value'
    assert some_list[index_stored_to + 1] == old_value


def test_insert_out_of_range(some_list):
    """When insert to the index out of range, the item inserted to the end of list"""
    some_list.insert(100, 'added_value')
    assert some_list[-1] == 'added_value'
