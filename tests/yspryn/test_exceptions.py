import pytest
import sys
sys.path.append('./tests/yspryn')


def test_index_error():
    a = list()
    b = [1, 23, 'no']

    with pytest.raises(IndexError):
        a[12]

    with pytest.raises(IndexError):
        b[5]

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        a = 78/0


def test_attribute_error():
    a = "hello world"
    with pytest.raises(AttributeError):
        a.lengh()


def test_key_error():
    test_dict = {1: 10, 2: 20, 3: 30}
    with pytest.raises(KeyError):
        test_dict[4]


def test_name_error():
    my_list = [1, 2, 3, 55]
    a1 = 10
    with pytest.raises(NameError):
        my_lists[1]
    with pytest.raises(NameError):
        a11 + 6


def test_syntax_error():
    with pytest.raises(SyntaxError):
        import my_test_module

def test_type_error():
    with pytest.raises(TypeError):
        len(50)


def test_stop_iteration():
    with pytest.raises(StopIteration):
        iterator = iter([1, 2, 3])
        while True:
            next_value = next(iterator)


def test_import_error():
    with pytest.raises(ImportError):
       import non_existent_module
