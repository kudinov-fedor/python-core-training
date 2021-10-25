from akaiafiuk.acceptable_password import is_acceptable_password
from akaiafiuk.backward_string import backward_string
from akaiafiuk.beginning_zeros import beginning_zeros
from akaiafiuk.end_zeros import end_zeros
from akaiafiuk.first_word_simplified import first_word
from akaiafiuk.max_digit import max_digit
from akaiafiuk.multiply import multiply_two
from akaiafiuk.nearest_value import nearest_value
from akaiafiuk.number_length import number_length
from akaiafiuk.remove_all_before import remove_all_before
from akaiafiuk.replace_first import replace_first
import pytest


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


def test_first_word():
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"


def test_max_digit():
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1


@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 6),
    (2, 2, 4),
    (1, 0, 0)
])
def test_multiply_two(a, b, expected):
    assert multiply_two(a, b) == expected


def test_nearest_value():
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1


@pytest.mark.parametrize("number, result", [
    (10, 2),
    (0, 1),
    (4, 1),
    (44, 2)
])
def test_number_length(number, result):
    assert number_length(number) == result


def test_remove_all_before():
    assert remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
    assert remove_all_before([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4]
    assert remove_all_before([1, 1, 5, 6, 7], 2) == [1, 1, 5, 6, 7]
    assert remove_all_before([], 0) == []
    assert remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7) == [7, 7, 7, 7, 7, 7, 7, 7, 7]


def test_replace_first():
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
