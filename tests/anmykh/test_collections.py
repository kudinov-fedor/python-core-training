some_str = "abcd"
some_tuple = "a", "b", "c", "d"
some_list = ["a", "b", "c", "d"]
some_set = {"a", "b", "c", "d"}
some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}
b = [1, 2, 3, 4]


def test_modify_collection():
    b[3] = "abc"
    assert b[3] == "abc"


def test_modify_collection2():
    a, *tail = some_str
    assert tail == ['b', 'c', 'd']


def test_modify_collection3():
    *head, d = some_dict
    assert head == ['a', 'b', 'c']

