import pytest

data = ["cat", "dog", "", None, False, 0, 1, -2, True]


@pytest.mark.parametrize(["param", "result"], [
    (bool(set()), False),
    (bool(-0.1), True),
    (bool({"a": 123}), True),
    (len([False, ]) > 0, True),
    (not 0, True),
    (not (1, 2, 3), False),
    ("it is true" if True else "it is false", "it is true"),
    ("it is true" if [] else "it is false", "it is false"),
    # take first True item, or last
    (1 or 3, 1),
    (None or 0 or "" or [] or "at last some value", "at last some value"),
    # take first False item, or last
    (1 and 3, 3),
    (1 and "abc" and 0.0 and "some value", 0.0),
    # priority
    ("" or "Some" and {} == {}, True),
    ({} or "" and "Some", ""),
    ({} and "" or "Some", "Some"),
    (False or "" and 123, ""),
    (False and "" or 123, 123),
    # if all are true
    (all(["a", 0, True, (1, 2, 3)]), False),
    (all(["a", 1, True, (1, 2, 3)]), True),
    # if at least 1 is true
    (any(["", 0, False, (), None]), False),
    (any(["", 1, False, (), None]), True),
    (list(filter(None, data)) == ['cat', 'dog', 1, -2, True], True),
    (list(filter(lambda i: isinstance(i, str), data)) == ['cat', 'dog', ''], True)
])
def test_assertion(param, result):
    assert param is result
