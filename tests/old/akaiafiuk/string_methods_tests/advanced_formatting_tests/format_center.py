def test_center_string():
    """Center string using format"""
    assert '{:^10}'.format('test') == '   test   '


def test_center_uneven():
    """When there's uneven split of the characters the extra character will be added on the right side"""
    assert '{:^6}'.format('zip') == ' zip  '
