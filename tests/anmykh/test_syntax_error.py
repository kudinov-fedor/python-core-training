import pytest

def test_syntax_error():
    sad = {"abc": 123}
    with pytest.raises(SyntaxError):
        sad{"abc"}
