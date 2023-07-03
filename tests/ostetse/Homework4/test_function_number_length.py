from tests.ostetse.Homework4.define_function_number_length import number_length


def test_number_length():
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2

