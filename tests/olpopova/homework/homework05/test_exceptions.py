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
    sequence = ''
    my_iterator = iter(sequence)
    with pytest.raises(StopIteration):
        next(my_iterator)
