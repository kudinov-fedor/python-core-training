import pytest


@pytest.fixture
def some_list() -> list:
    return [1, 2, 3, 'a', 'b', 'c']


def test_clear(some_list):
    """clear() method removes all items from the list"""
    some_list.clear()
    assert some_list == []


def test_pop_default(some_list):
    """By default, last item is removed and returned"""
    original_length = len(some_list)
    popped = some_list.pop()
    assert popped == 'c'
    assert len(some_list) == original_length - 1


@pytest.mark.parametrize('index, popped_value, result_list', [
    (-1, 'c', [1, 2, 3, 'a', 'b']),  # Pop last element. Same as calling with no argument
    (0, 1, [2, 3, 'a', 'b', 'c']),   # Pop first element.
    (3, 'a', [1, 2, 3, 'b', 'c'])    # Pop an element from the middle.
])
def test_pop_with_defined_index(some_list, index, popped_value, result_list):
    """Test popping element with index defined. Index is in range of the given list."""
    x = some_list.pop(index)
    assert x == popped_value
    assert some_list == result_list


@pytest.mark.parametrize('index, exception, error_text', [
    (100, IndexError, 'pop index out of range'),
    (-100, IndexError, 'pop index out of range'),
    ('a', TypeError, "'str' object cannot be interpreted as an integer"),
])
def test_pop_negative_cases(some_list, index, exception, error_text):
    """Test that error is raised when calling pop with an invalid arguemnt"""
    with pytest.raises(exception, match=error_text):
        some_list.pop(index)


def test_remove():
    """Removes the first occurrence of the element"""
    fruits = ['apple', 'banana', 'apple', 'cherry']
    fruits.remove('apple')
    assert fruits == ['banana', 'apple', 'cherry']


def test_remove_negative(some_list):
    """Value error is raised if the element is not in the list"""
    with pytest.raises(ValueError):
        some_list.remove('apple')
