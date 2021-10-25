import pytest

from vpavly.m1.acceptable_password import is_acceptable_password
from vpavly.m1.backward_string import backward_string
from vpavly.m1.begin_zeros import beginning_zeros
from vpavly.m1.end_zeros import end_zeros
from vpavly.m1.first_word import first_word
from vpavly.m1.max_digit import max_digit
from vpavly.m1.multiply import mult_two
from vpavly.m1.nearest_value import nearest_value
from vpavly.m1.number_length import number_length
from vpavly.m1.remove_all_before import remove_all_before
from vpavly.m1.replace_first import replace_first
from vpavly.m1.split_pairs import split_pairs


# 1 #
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (5, 2, 10),
    (-4, 2, -8),
    (0, 5, 0)
])
def test_mult_two(a, b, expected):
    assert mult_two(a, b) == expected


# 2 #
@pytest.mark.parametrize('a, expected', [('Hello world', 'Hello'), ('', ''), ('1', '1')])
def test_first_word(a, expected):
    assert first_word(a) == expected


# 3 #
@pytest.mark.parametrize('a, expected', [('test_pass', True), ('pass', False), ('qwerty1', True)])
def test_is_acceptable_password(a, expected):
    assert is_acceptable_password(a) == expected


# 4 #
@pytest.mark.parametrize('a, expected', [(10, 2), (1, 1), (987654, 6)])
def test_number_length(a, expected):
    assert number_length(a) == expected


# 5 #
@pytest.mark.parametrize('a, expected', [(100, 2), (0, 1), (1, 0)])
def test_end_zeros(a, expected):
    assert end_zeros(a) == expected


# 6 #
@pytest.mark.parametrize('a, expected', [('asd', 'dsa'), ('a', 'a'), ('123', '321')])
def test_backward_string(a, expected):
    assert backward_string(a) == expected


# 7 #
@pytest.mark.parametrize('a, b, expected', [([1, 2, 3, 4, 5], 4, [4, 5])])
def test_remove_all_before(a, b, expected):
    assert list(remove_all_before(a, b)) == expected


# 8 #
@pytest.mark.parametrize('a, expected', [('001', 2), ('0', 1), ('', 0)])
def test_begin_zeros(a, expected):
    assert beginning_zeros(a) == expected


# 9 #
@pytest.mark.parametrize('a, expected', [([1, 2, 3], [2, 3, 1]), ([1], [1]), ([], [])])
def test_replace_first(a, expected):
    assert replace_first(a) == expected


# 10 #
@pytest.mark.parametrize('a, expected', [(123, 3), (1, 1), (1000, 1)])
def test_max_digit(a, expected):
    assert max_digit(a) == expected


# 11 #
@pytest.mark.parametrize('a, expected', [('abcdef', ['ab', 'cd', 'ef']), ('abc', ['ab', 'c_']), ('', [])])
def test_split_pairs(a, expected):
    assert split_pairs(a) == expected


# 12 #
@pytest.mark.parametrize('a, b, expected', [
    ({4, 7, 10, 11, 12, 17}, 9, 10),
    ({4, 7, 10, 11, 12, 17}, 8, 7),
    ({4, 8, 10, 11, 12, 17}, 9, 8),
    ({-1, 2, 3}, 0, -1)])
def test_nearest_value(a, b, expected):
    assert nearest_value(a, b) == expected

# 13 #
