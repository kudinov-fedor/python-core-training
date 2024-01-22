import importlib

import pytest

from nataliia_romanchuk.Classes import Cats


def test_attribute_error():
    cat = Cats('Pushok', 10)
    print(cat.meow())
    print(cat.sleep())
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
        5 / 0


def test_file_not_found_error():
    package_name = "nataliia_romanchuk"
    with pytest.raises(FileNotFoundError):
        with importlib.resources.open_text(package_name, "Teext.txt") as file:
            content = file.read()
            print(content)


def test_module_not_found_error():
    package_name = "nataliia_romanchukkkkkkk"
    with pytest.raises(ModuleNotFoundError):
        with importlib.resources.open_text(package_name, "Text.txt") as file:
            content = file.read()
            print(content)


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


def test_arithmetic_error():
    with pytest.raises(ArithmeticError):
        1 / 0


def test_key_error():
    my_dict = {"key": "value"}
    with pytest.raises(KeyError):
        my_dict["nonexistent_key"]
