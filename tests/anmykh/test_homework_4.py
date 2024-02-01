import pytest


def test_assertion_error():
    with pytest.raises(AssertionError):
        assert 0 <= (5 is True) is True


def test_attribute_error():
    sad = (2, 1, 43, 1)
    with pytest.raises(AttributeError):
        sad.pop


def test_attribute_error2():
    sad = (2, 1, 43, 1)
    with pytest.raises(AssertionError):
        assert 0


def test_syntax_error2():
   with pytest.raises(SyntaxError):
       from tests.anmykh import import_file


def test_value_error():
    sad = (2, 12, 12, 4)
    with pytest.raises(ValueError):
        sad.index(0)


def test_module_not_found():
    with pytest.raises(Exception):
        import import_file


def test_type_error():
    with pytest.raises(Exception):
        assert 10 / "sad"


def test_arithmetic_error():
    with pytest.raises(Exception):
        assert 10 / 0

