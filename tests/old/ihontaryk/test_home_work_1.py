import pytest


@pytest.mark.parametrize("input1, expected_result",
                         [("abs", str),
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
                          ])
def test_types(input1, expected_result):
    """verify types of data"""
    assert type(input1) == expected_result


@pytest.mark.parametrize("input1, input2",
                         [
                             (("d", "o", "g"), ("d", "a", "y")),
                             ("dog", "day"),
                             ([1, 3], [1, 2]),
                             (1, -1)
                         ])
def test_comparison(input1, input2):
    """verify comparison"""
    assert input1 > input2


@pytest.mark.parametrize("input1, input2",
                         [
                             ([1, 2], [1, 2]),
                             ({1, 2}, {1, 2}),
                             ((1, 3), (1, 2))
                         ])
def test_different_ids(input1, input2):
    """verify different ids"""
    assert id(input1) != id(input2)


@pytest.mark.parametrize("input1, input2",
                         [
                             ("a", "a"),
                             (1, 1),
                             ((1, 2), (1, 2))
                         ])
def test_same_ids(input1, input2):
    """verify same ids"""
    assert id(input1) == id(input2)
