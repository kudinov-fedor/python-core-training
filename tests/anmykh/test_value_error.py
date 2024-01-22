import pytest

def test_value_error():
    sad = (2, 12, 12, 4)
    with pytest.raises(ValueError):
        sad.index(0)
