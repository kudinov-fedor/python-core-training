some_dict = {"a": 123, "b": 456, "c": 789}
some_dict_2 = {"c": 789, "a": 123, "b": 456}


def test_dict_equality():
    assert some_dict == some_dict_2
    assert some_dict is not some_dict_2


def test_dict_methods():
    copied_dict = dict(some_dict)
    assert copied_dict.get("invalid") is None
    copied_dict.clear()
    assert copied_dict == {}
    copied_dict.setdefault("a", 10)
    assert copied_dict["a"] == 10


def test_dict_comprehension():
    test_dict = {k: v for k, v in some_dict.items() if k <= "b"}
    assert len(test_dict) == 2
    assert test_dict == {"a": 123, "b": 456}
