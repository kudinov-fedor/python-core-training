import importlib

import pytest

from nataliia_romanchuk.Cats import Cats


def test_attribute_error():
    cat_name = 'Pushok'
    cat_age = 10
    cat = Cats(cat_name, cat_age)
    expected_meow_output = f"Cat {cat.name} says Meow for {cat.age} years!"
    assert cat.meow() == expected_meow_output
    expected_sleep_output = f"Cat {cat.name} is sleeping. Shhhhhhhh!"
    assert cat.sleep() == expected_sleep_output
    with pytest.raises(AttributeError):
        cat.woof()

def test_index_error():
    list = [1, 2]
    with pytest.raises(IndexError):
        list[3]


def test_assertion_error():
    with pytest.raises(AssertionError):
        assert False, "Expected AssertionError"


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_arithmetic_error():
    with pytest.raises(ArithmeticError):
        1 / 0


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        importlib.resources.open_text("nataliia_romanchuk", "Teext.txt")


def test_module_not_found_error():
    with pytest.raises(ModuleNotFoundError):
        importlib.resources.open_text("nataliia_romanchukkkkkkk", "Text.txt")


def test_import_error():
    with pytest.raises(ImportError):
        import unknown_module


def test_value_error():
    with pytest.raises(ValueError):
        int('qwerty')


def test_memory_error():
    with pytest.raises(MemoryError):
        bytearray(100 ** 9)


def test_name_error():
    with pytest.raises(NameError):
        variable


def test_type_error():
    with pytest.raises(TypeError):
        "5" + 2


def test_key_error():
    my_dict = {"key": "value"}
    with pytest.raises(KeyError):
        my_dict["a_key"]
