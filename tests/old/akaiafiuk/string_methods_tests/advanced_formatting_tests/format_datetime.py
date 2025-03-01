from datetime import datetime


def test_format_datetime():
    """Format datetime object inline"""
    assert '{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)) == '2001-02-03 04:05'


def test_fstring_datetime():
    """Format datetime object inline using literal"""
    assert f"{datetime(2001, 2, 3, 4, 5):%Y-%m-%d %H:%M}" == '2001-02-03 04:05'


def test_format_using_datetime():
    """Format datetime object inline using datetime object itself"""
    assert datetime(2001, 2, 3, 4, 5).strftime("%Y-%m-%d %H:%M") == '2001-02-03 04:05'
