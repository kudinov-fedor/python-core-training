def test_truncate_old_school():
    """The number behind a . in the format specifies the precision of the output."""
    assert '%.5s' % ('xylophone', ) == 'xylop'


def test_truncate_format():
    """The number behind a . in the format specifies the precision of the output."""
    assert '{:.5}'.format('xylophone') == 'xylop'


def test_truncate_and_padding():
    """combine truncating and padding"""
    assert '{:10.5}'.format('xylophone') == 'xylop     '
