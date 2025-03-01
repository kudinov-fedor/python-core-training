import pytest


def test_concatenate_positive():
    """Concatenate two lists using + operator"""
    result = [1, 2, 3] + [3, 4, 5, 6]
    assert result == [1, 2, 3, 3, 4, 5, 6]


def test_concatenate_in_place():
    """Concatenate two lists in-place using += operator"""
    some_list = [1, 2, 3]
    some_list += [4, 5, 6]
    assert some_list == [1, 2, 3, 4, 5, 6]


def test_concatenate_in_place_second_link():
    """Concatenate two lists in-place using += operator"""
    some_list = [1, 2, 3]
    second_link = some_list
    some_list += [4, 5, 6]
    assert some_list == [1, 2, 3, 4, 5, 6]
    assert second_link == [1, 2, 3, 4, 5, 6]
    assert second_link is some_list


@pytest.mark.parametrize(
    "s1, s2, expected_result", [
        ([1, 2, 3], (3, 4, 5), [1, 2, 3, 3, 4, 5]),
        ([1, 2, 3], (3, 4, 5), {1, 2, 3, 3, 4, 5}),
        ([1, 2, 3], (3, 4, 5), 1),
        ([1, 2, 3], (3, 4, 5), 'abcd'),
    ]
)
def test_concatenation_negative_case(s1, s2, expected_result):
    """Concatenation if not possible if parameter is not a list"""
    with pytest.raises(TypeError, match='can only concatenate list'):
        s1 + s2
