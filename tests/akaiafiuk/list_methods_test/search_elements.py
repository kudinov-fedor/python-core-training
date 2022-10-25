import pytest


@pytest.mark.parametrize('element, count', [
    (1, 2),     # count of element occurrence in the list
    (777, 0)    # if the element absent, 0 is returned
])
def test_count(element, count):
    """count() returns count of element occurrence in the list"""
    x = [1, 2, 3, 4, 1, -1]
    assert x.count(element) == count


def test_index_basic():
    """index() returns index of first occurrence in the list"""
    x = [2, 1, 3, 4, 1, -1]
    assert x.index(1) == 0


@pytest.mark.parametrize('element, start_at, index', [
    (1, 1, 1),     # start index included
    (1, 3, 5)      # search for index starts from 3 and continues till the end
])
def test_index_start(element, start_at, index):
    """Can specify start index as a first argument"""
    x = [1, 1, 1, 3, 4, 1, -1]
    assert x.index(element, start_at) == index


def test_index_end():
    """Can specify the end index parameter as a third argument"""
    x = [1, 1, 1, 3, 4, 1, -1]
    assert x.index(3, 0, 4) == 3


def test_index_element_absent():
    """ValueError is raised if the element is not in the list or outside start and stop indexes"""
    x = [1, 1, 1, 3, 4, 1, -1]
    value = 1
    with pytest.raises(ValueError, match=f"{value} is not in list"):
        x.index(value, 3, 5)


def test_index_no_keyword_args():
    """Keyword arguments are not accepted"""
    x = [1, 1, 1, 3, 4, 1, -1]
    with pytest.raises(TypeError, match="takes no keyword arguments"):
        x.index(3, stop=4)
