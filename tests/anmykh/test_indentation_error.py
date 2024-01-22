import pytest

def test_indentation_error_():
    sad = (2, 12, 12, 4)
    with pytest.raises(IndentationError):
        sad[0]
