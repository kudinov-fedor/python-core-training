import pytest

data1 = [
    ("abs", str),
    ((1), int),
    (0, int),
    (000, int),
    (-1.1, float),
    ([], list),
    ([1], list),
    ({"a": 1}, dict),
    ({}, dict),
    ((1,), tuple),
    (True, bool),
    ({1, 2, 3}, set)
]


@pytest.mark.parametrize("input1, expected_result", data1)
def test_types(input1, expected_result):
    """verify types of data"""
    assert type(input1) == expected_result


data2 = [
    (("d", "o", "g"), ("d", "a", "y")),
    ("dog", "day"),
    ([1, 3], [1, 2]),
    (1, -1)
]


@pytest.mark.parametrize("input1, input2", data2)
def test_comparison(input1, input2):
    """verify types of comparison"""
    assert input1 > input2
