import pytest

def test_zero_division_error():
    a = 123
    with pytest.raises(ZeroDivisionError):
        x = a / 0

def test_index_error():
    a = [1, 2, 3, 4]
    with pytest.raises(IndexError):
        x= a[len(a) + 1]

def test_key_error():
    countries = {"USA": "Washington", "UK": "London", "France": "Paris"}
    with pytest.raises(KeyError):
        countries["ABC"]

def test_syntax_error():
    x = 123
    with pytest.raises(AttributeError):
        x.len()

def test_io_error():
    x = "test.txt"
    with pytest.raises(FileNotFoundError):
        with open(x, "r") as file:
            content = file.read()
            print(content)

def test_value_error():
    x = "Windows"
    with pytest.raises(ValueError):
        x = int(x)