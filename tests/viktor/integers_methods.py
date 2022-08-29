import pytest


@pytest.mark.parametrize("val1, val2, expected", [
    (5, 5, 10),
    (20, 20, 40),
    (30, 35, 65)
])
def test_operator_plus(val1, val2, expected):
    assert val1 + val2 == expected



@pytest.mark.parametrize("val1, val2, exp", [
    (4, 6, 24),
    (5, 5, 25),
    (8, 8, 64)
])
def test_operatorMultiply(val1, val2, exp):
    assert val1 * val2 == exp


@pytest.mark.parametrize("val1, val2, exp", [
    (8, 6, 2),
    (6, 5, 1),
    (9, 8, 1)
])
def test_operatorDevidePerc(val1, val2, exp):
    assert val1 % val2 == exp




@pytest.mark.parametrize("val1, val2, expected", [
    (10, 8, 1),
    (20, 10, 2),
    (100, 51, 1)
])
def test_operator_devide(val1, val2, expected):
    assert val1 // val2 == expected

#
@pytest.mark.parametrize("data, val, start_position, end_position, expected", [
    ("I love Python", "o", 5, 20, 11),
    ("I love Python", "o", 0, 20, 3),
    ("I love Python", "r", 3, 5, -1),
    ("I love Python", "er", 10, 15, -1)
])

def test_find(data, val, start_position, end_position, expected):
    assert data.find(val, start_position, end_position) == expected

@pytest.mark.parametrize("falsy_vals", [
    0, "", [], (), {}, None, False, 0.0
])
def test_falsy_vals(falsy_vals):
    with pytest.raises(AssertionError):
        assert falsy_vals