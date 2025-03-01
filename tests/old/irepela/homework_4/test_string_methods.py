test_str = "some good word"
hello_world_str = "hello world"


def test_string_find():
    not_found_index = "some good word".find("some not existing string")
    o_index = test_str.find("o")
    assert o_index == 1
    assert not_found_index == -1


def test_string_utils():
    assert hello_world_str.capitalize() == "Hello world"
    assert hello_world_str.title() == "Hello World"
