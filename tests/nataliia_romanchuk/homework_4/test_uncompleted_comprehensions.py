from itertools import tee

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
    generator, generator1, generator2, generator3 = tee((i for i in some_list), 4)

    list_result = list(generator1)
    assert list_result == some_list

    set_result = set(generator2)
    assert set_result == set(some_list)

    dict_result = dict((i, i * 2) for i in generator3)
    assert dict_result == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

    tuple_result = tuple(generator)
    assert tuple_result == tuple(some_list)


# if generator expression is 1 and only 1 parameter,
# parenthesis can be avoided
def test_generator_comprehensions():
    generator_object, generator_object1, generator_object2, generator_object3 = tee((i for i in some_list), 4)
    assert list(generator_object) == [1, 2, 3, 4, 5]
    assert set(generator_object1) == {1, 2, 3, 4, 5}
    assert dict((i, i * 2) for i in generator_object2) == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
    assert tuple(generator_objec3) == (1, 2, 3, 4, 5)


# comprehensions with filtration and item modification
def test_comprehensions_with_filtration_and_modification():
    assert [i * 2 for i in some_list if i <= 3] == [2, 4, 6]

    generator_object = (i * 2 for i in some_list if i <= 3)
    assert list(generator_object) == [2, 4, 6]

    assert {i * 2 for i in some_list if i <= 3} == {2, 4, 6}

    assert {i: i * 2 for i in some_list if i <= 3} == {1: 2, 2: 4, 3: 6}


# process dict in comprehensions, same as during iteration
[some_dict[k] * 2 for k in some_dict if some_dict[k] <= 2]
[k for k in some_dict if some_dict[k] <= 2]

[i[1] * 2 for i in some_dict.items() if i[1] <= 2]
[i[0] for i in some_dict.items() if i[1] <= 2]
[k for k, v in some_dict.items() if v <= 2]
[k for (k, v) in some_dict.items() if v <= 2]

{i[0]: i[1] for i in some_dict.items()}
{k: v for k, v in some_dict.items()}
{k: v for k, v in some_dict.items() if v <= 2}
{k * 2: v * 2 for k, v in some_dict.items() if v <= 2}

# collect data
data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]

ages = {i["age"] for i in data}
names = {i["name"] for i in data}
