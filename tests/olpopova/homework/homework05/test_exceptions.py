import pytest


def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        5 / 0


def test_type_error():
    with pytest.raises(TypeError):
        6 / "gh"


def test_index_out_error():
    with pytest.raises(IndexError):
        [][1]


def test_stop_iter_error():
    with pytest.raises(StopIteration):
        sequence = 'jghfy'
        my_iterator = iter(sequence)
        while next(my_iterator):
            print(next(my_iterator))
