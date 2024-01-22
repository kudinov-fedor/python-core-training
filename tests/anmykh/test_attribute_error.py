import pytest


def test_attribute_error():
    sad = (2, 1, 43, 1)
    with pytest.raises(AttributeError):
        sad.pop(0)
