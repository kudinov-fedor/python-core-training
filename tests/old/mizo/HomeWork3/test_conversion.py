import pytest


@pytest.mark.parametrize("bool_value, expected", [
    (True, "True"),
    (False, "False")
])
def test_bool_to_str(bool_value, expected):
    bool_str = str(bool_value)
    assert bool_str == expected


"""
tuple "abc"
"""


def test_string_to_tuple():
    tuple_value = ("a", "b", "c")
    result = tuple("abc")
    assert result == tuple_value


def test_list_paired():
    my_actual_input = list(zip(["a", "b", "c"], [1, 2, 3]))
    my_expected_output = [("a", 1), ("b", 2), ("c", 3)]
    assert my_actual_input == my_expected_output


"""
list(enumerate(["a", "b", "c"]))
"""


def test_enumerate():
    assert list(enumerate(["a", "b", "c"], 1)) == [(1, "a"), (2, "b"), (3, "c")]
