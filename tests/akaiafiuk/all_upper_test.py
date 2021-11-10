from akaiafiuk.all_upper_i import is_all_upper


def test_is_all_upper():
    assert is_all_upper('ALL UPPER') is True
    assert is_all_upper('all lower') is False
    assert is_all_upper('mixed UPPER and lower') is False
    assert is_all_upper('') is True
    assert is_all_upper('     ') is True
    assert is_all_upper('444') is True
    assert is_all_upper('55 55 5') is True
