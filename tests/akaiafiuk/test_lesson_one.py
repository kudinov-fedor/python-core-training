from akaiafiuk.AcceptablePasswordI import is_acceptable_password
from akaiafiuk.backward_string import backward_string
from akaiafiuk.beginning_zeros import beginning_zeros
from akaiafiuk.end_zeros import end_zeros


def test_is_acceptable_password():
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False


def test_backward_string():
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'


def test_beginning_zeros():
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4


def test_end_zeros():
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2


