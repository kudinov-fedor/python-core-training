def test_bool():
    some_bool = bool()

    assert isinstance(some_bool, int)
    assert isinstance(some_bool, bool)
    assert isinstance(some_bool, (int, float, str))
    assert not isinstance(some_bool, (float, str))
    assert isinstance(some_bool, object)
    assert type(some_bool) is bool
    assert type(some_bool) is not int
    assert bool("abs") is True
    assert issubclass(bool, int)
    assert issubclass(bool, bool)
    assert not issubclass(bool, float)
    assert callable(bool)
    assert not callable(some_bool)


def test_len():
    some_str = "Hello python code!"
    some_dict = {1: "a", 2: [1, 2, 3]}
    some_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    some_tuple = ("x", "y", "z")
    some_set = {1, 33, 67, 1, 1, 90}
    some_range = range(90)

    assert len(some_str) == 18
    assert len(some_dict) == 2
    assert len(some_list) == 7
    assert len(some_tuple) == 3
    assert len(some_set) == 4
    assert len(some_range) == 90
