from typing import List, Dict

some_list = [0, 1, 2, 3, 4, 5]
some_dict = {"a": 1, "b": 2, "c": 3}


def list_comp(x: List):
    my_list = [i for i in x]
    return my_list


def set_comp(x: List):
    my_set = {i * 2 for i in x if i <= 1}
    return my_set


def dict_comp(x: List):
    my_dict = {i: i * 2 for i in x}
    return my_dict


def dict_comp1(y: Dict):
    my_dict = {k * 2: v * 2 for k, v in y.items() if v <= 2}
    return my_dict


def gen_comp(x: List):
    my_generator = (i * i for i in x if i >= 3)
    for i in my_generator:
        yield i


def test_assert():
    assert list_comp(some_list) == [i for i in range(10) if i <= 5]
    assert set_comp(some_list) == {0, 2}
    assert dict_comp(some_list) == {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
    assert dict_comp1(some_dict) == {'aa': 2, 'bb': 4}
    assert list(gen_comp(some_list)) == [9, 16, 25]
    assert set(gen_comp(some_list)) == {9, 16, 25}
