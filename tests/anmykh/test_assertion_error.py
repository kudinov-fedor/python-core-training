import pytest


def test_attribute_error():
    with pytest.raises(AssertionError):
        assert 0 <= (5 == True) == True
