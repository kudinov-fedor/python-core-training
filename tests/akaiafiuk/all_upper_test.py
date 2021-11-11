import pytest
from akaiafiuk.all_upper_i import is_all_upper, is_all_upper_v2, is_all_upper_v3, is_all_upper_v4


@pytest.mark.parametrize("func", [
    is_all_upper,
    is_all_upper_v2,
    is_all_upper_v3,
    is_all_upper_v4
])
def test_is_all_upper(func):
    assert func('ALL UPPER')
    assert not func('all lower')
    assert not func('mixed UPPER and lower')
    assert func('')
    assert func('     ')
    assert func('444')
    assert func('55 55 5')
