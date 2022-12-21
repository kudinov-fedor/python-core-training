def test_rsplit_no_args():
    """rplit with no arguments splits using space as a separator. Works just like split."""
    assert "Hello World".rsplit() == ['Hello', 'World']


def test_rsplit_separator():
    """rplit with no arguments splits using space as a separator. Works just like split."""
    assert "Hello, World".rsplit(', ') == ['Hello', 'World']


def test_rsplit_max_split():
    """max_split second arg is used to specify number of splits. Len of list will be max_split + 1
    Difference with split is that splitting starts from the right side
    """
    assert "Hello World !".rsplit(' ', 1) == ['Hello World', '!']
