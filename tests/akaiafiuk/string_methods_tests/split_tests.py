import pytest


def test_split_no_args():
    """Split with no arguments splits using space as a separator."""
    assert "Hello World".split() == ['Hello', 'World']


def test_split_separator():
    """Split with no arguments splits using space as a separator."""
    assert "Hello, World".split(', ') == ['Hello', 'World']


def test_split_max_split():
    """max_split second arg is used to specify number of splits. Len of list will be max_split + 1"""
    assert "Hello World !".split(' ', 1) == ['Hello', 'World !']
