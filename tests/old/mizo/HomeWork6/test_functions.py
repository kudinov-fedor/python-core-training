from mizo.task_functions import (my_simple_function_with_required_params, with_optional_parameters,
                                 unlimited_positional, unlimited_named)


def test_my_simple_function():
    res = my_simple_function_with_required_params(10, num2=10.4)
    expected_output = 104.0
    assert res == expected_output


def test_with_optional_parameters():
    res1 = with_optional_parameters(a=123, b="hello")
    assert res1 == (123, "hello")
    res2 = with_optional_parameters(a=123)
    assert res2 == (123, "hi")


def test_unlimited_positional():
    res_unlimited_pos = unlimited_positional(1, 2, 3, some="val")
    assert res_unlimited_pos == (1, (2, 3), "val")
    res_unlimited_pos2 = unlimited_positional(1)
    assert res_unlimited_pos2 == (1, (), "val")
    res_unlimited_pos3 = unlimited_positional(1, 2, 3, 4, 5, 6)
    assert res_unlimited_pos3 == (1, (2, 3, 4, 5, 6), "val")


def test_unlimited_named():
    res_unlimited_named1 = unlimited_named(1)
    assert res_unlimited_named1 == (1, "val", {})
    res_unlimited_named2 = unlimited_named(some="123", a=456)
    assert res_unlimited_named2 == (456, "123", {})
    res_unlimited_named3 = unlimited_named(a=100, b=200, c=300, some="Testing", x="abc")
    assert res_unlimited_named3 == (100, "Testing", {"b": 200, "c": 300, "x": "abc"})
    res_unlimited_named4 = unlimited_named(a=1, some="Hello", x=10, y=20)
    assert res_unlimited_named4 != (42, "Hello", {"x": 10, "y": 20})
