from irepela.homework_10.recreate_generators import my_zip, my_enumerate, my_filter, my_map


def test_recreate_generators():

    a = ["a", "b", "c"]
    b = ["x", "y", "z"]

    assert list(zip(a, b)) == [("a", "x"), ("b", "y"), ("c", "z")]
    assert list(zip(a)) == [("a",), ("b",), ("c",)]
    assert list(my_zip(a, b)) == [("a", "x"), ("b", "y"), ("c", "z")]
    assert list(my_zip(a)) == [("a",), ("b",), ("c",)]

    assert list(enumerate(a)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(enumerate(a, start=2)) == [(2, "a"), (3, "b"), (4, "c")]
    assert list(my_enumerate(a)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(my_enumerate(a, start=2)) == [(2, "a"), (3, "b"), (4, "c")]

    a = [0, 1, 2, 0, 2, 3]
    assert list(filter(None, a)) == [1, 2, 2, 3]
    assert list(filter(lambda i: i < 2, a)) == [0, 1, 0]
    assert list(my_filter(None, a)) == [1, 2, 2, 3]
    assert list(my_filter(lambda i: i < 2, a)) == [0, 1, 0]

    a = [0, 1, 2, 0, 2, 3]
    b = [3, 1, 2, 2, 1, 4]
    add = lambda a, b: a + b

    assert list(map(str, a)) == ["0", "1", "2", "0", "2", "3"]
    assert list(map(add, a, b)) == [3, 2, 4, 2, 3, 7]

    assert list(my_map(str, a)) == ["0", "1", "2", "0", "2", "3"]
    assert list(my_map(add, a, b)) == [3, 2, 4, 2, 3, 7]
