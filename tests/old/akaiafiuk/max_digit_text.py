from akaiafiuk.max_digit import max_digit, max_digit_using_max


def test_max_digit():
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1


def test_max_digit_using_max():
    assert max_digit_using_max(0) == 0
    assert max_digit_using_max(52) == 5
    assert max_digit_using_max(634) == 6
    assert max_digit_using_max(1) == 1
    assert max_digit_using_max(10000) == 1
