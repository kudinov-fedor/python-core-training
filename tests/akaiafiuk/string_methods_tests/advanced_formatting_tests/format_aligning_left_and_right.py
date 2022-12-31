def test_align_right_to_specific_len_old():
    """Old school syntax to define that a value should be padded to a specific length"""
    assert '%10s' % ('test',) == '      test'


def test_align_right_to_specific_len_new():
    """Old school syntax to define that a value should be padded to a specific length"""
    assert '{:>10}'.format('test') == '      test'


def test_align_left_to_specific_len_old():
    """Old school syntax to define that a value should be padded to a specific length"""
    assert '%-10s' % ('test',) == 'test      '


def test_align_left_to_specific_len_new():
    """Old school syntax to define that a value should be padded to a specific length"""
    assert '{:10}'.format('test') == 'test      '


def test_align_with_char_selection():
    """With using .format can use padding along with character selection"""
    assert '{:_<10}'.format('test') == 'test______'


def test_align_with_char_selection_literal():
    """Just an example that can use formatting using a literal"""
    assert f'{"test":_<10}' == 'test______'
