# comprehensions
some_list = [1, 2, 3, 4, 5]
some_dict = {"a": 1, "b": 2, "c": 3}


def test_list_comprehension():
    result = [i * 2 for i in some_list if i <= 3]
    assert result == [2, 4, 6]


def test_generator_expression():
    generator = (i * 2 for i in some_list if i >= 3)
    assert next(generator) == 6
    assert next(generator) == 8
    assert next(generator) == 10
    items_left = [*generator]
    assert items_left == []


def test_dict_comprehension():
    result = [k for k in some_dict if some_dict[k] <= 2]
    assert result == ["a", "b"]
