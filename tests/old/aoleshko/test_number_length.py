from aoleshko.number_length import number_length


def test_number_length():
    assert number_length(123) == 3
    assert number_length(1234) == 4
