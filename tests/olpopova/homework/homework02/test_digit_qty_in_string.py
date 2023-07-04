from olpopova.homework.homework02.digit_qty_in_string import *


def test_digit_qty():
    for i in range(1, 50):
        val = int("9" * i)
        assert number_length(val) == number_length_with_log_10(val) == number_length_with_div_mod(val)
