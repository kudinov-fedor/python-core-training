# comprehensions
some_list = [1, 2, 3, 4, 5]
some_dict = {"a": 1, "b": 2, "c": 3}


def test_comprehensions():
    # generator expression
    generator_result = list(i for i in some_list)
    assert generator_result == some_list

    # list comprehension
    list_result = [i for i in some_list]
    assert list_result == some_list

    # set comprehension
    set_result = {i for i in some_list}
    assert set_result == set(some_list)

    # dict comprehension
    dict_result = {i: i * 2 for i in some_list}
    assert dict_result == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}


"""create generator object using generator expression and unpack items form it into list, set, dict, tuple"""


def test_generator_expression_unpacking():
    generator1 = (i for i in some_list)
    list_result = list(generator1)
    assert list_result == some_list

    generator2 = (i for i in some_list)
    set_result = set(generator2)
    assert set_result == set(some_list)

    generator3 = (i for i in some_list)
    dict_result = dict((i, i * 2) for i in generator3)
    assert dict_result == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

    generator = (i for i in some_list)
    tuple_result = tuple(generator)
    assert tuple_result == tuple(some_list)


def test_generator_comprehensions():
    generator_list = (i for i in some_list)
    assert list(generator_list) == [1, 2, 3, 4, 5]

    generator_set = (i for i in some_list)
    assert set(generator_set) == {1, 2, 3, 4, 5}

    generator_dict = (i for i in some_list)
    assert dict((i, i * 2) for i in generator_dict) == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

    generator_tuple = (i for i in some_list)
    assert tuple(generator_tuple) == (1, 2, 3, 4, 5)


def test_comprehensions_with():
    assert [i * 2 for i in some_list if i <= 3] == [2, 4, 6]
    generator_object = (i * 2 for i in some_list if i <= 3)
    assert list(generator_object) == [2, 4, 6]
    assert {i * 2 for i in some_list if i <= 3} == {2, 4, 6}
    assert {i: i * 2 for i in some_list if i <= 3} == {1: 2, 2: 4, 3: 6}
