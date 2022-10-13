import pytest


@pytest.mark.parametrize("inside, outside", [
    ([2, 1, 3, 4, 2], [1, 2, 2, 3, 4]),                              # ascending
    (['orange', 'apple', 'banana'], ['apple', 'banana', 'orange']),  # alphabetical
    (['orange', 'apple', 'Banana'], ['Banana', 'apple', 'orange']),  # case-sensitive
])
def test_sort_basic(inside, outside):
    """By default sorting is performed in ascending or alphabetic order"""
    some_list = inside
    some_list.sort()
    assert some_list == outside


@pytest.mark.parametrize("inside, outside", [
    ([2, 1, 3, 4, 2], [4, 3, 2, 2, 1]),                              # descending
    (['orange', 'apple', 'banana'], ['orange', 'banana', 'apple']),  # alphabetical
    (['orange', 'apple', 'Banana'], ['orange', 'apple', 'Banana']),  # case-sensitive
])
def test_sort_reverse(inside, outside):
    """Sorting is performed in descending or descending alphabetic order with argument reverse=True"""
    some_list = inside
    some_list.sort(reverse=True)
    assert some_list == outside


def test_sort_with_key():
    """Sort using key function. In this example sort by len descending."""
    some_list = ['a', 'bbb', 'dddd']
    some_list.sort(key=len, reverse=True)
    assert some_list == ['dddd', 'bbb', 'a']


def test_sort_with_lambda_key():
    """Sort with key as lambda function"""
    some_list = [2, -1, -100]
    some_list.sort(key=lambda i: i * i)
    assert some_list == [-1, 2, -100]


def test_reverse():
    """Reverse the list in place"""
    some_list = [2, -1, -100]
    some_list.reverse()
    assert some_list == [-100, -1, 2]
