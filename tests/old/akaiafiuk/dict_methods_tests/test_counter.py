import pytest
from collections import Counter


@pytest.fixture()
def ct():
    return Counter('abracadabra')


def test_representation(ct):
    """Creates a Counter object with set of inputted values as keys and occurrence count as value"""
    assert ct == Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})


def test_update(ct):
    """Updating counter updates count for existing keys and adds new"""
    ct.update('aaaaaazzzz')
    assert ct == Counter({'a': 11, 'z': 4, 'b': 2, 'r': 2, 'c': 1, 'd': 1})


def test_subtract(ct):
    """Can subtract occurrences count as well"""
    ct.subtract('abracadabra')
    assert ct == Counter({'a': 0, 'b': 0, 'r': 0, 'c': 0, 'd': 0})


def test_most_common(ct):
    """Can return most common values and their counts"""
    most_common = ct.most_common(2)
    assert isinstance(most_common, list)
    assert isinstance(most_common[0], tuple)
    assert len(most_common) == 2
    assert ct.most_common(2) == [('a', 5), ('b', 2)]


def test_elements(ct):
    """Elements method will return keys multiplied by their count in list format"""
    assert sorted(ct.elements()) == ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'd', 'r', 'r']
