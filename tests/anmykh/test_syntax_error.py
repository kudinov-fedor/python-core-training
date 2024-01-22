import pytest

def test_syntax_error():
    sad = {"abc": 123}
    with pytest.raises(SyntaxError):
        sad{"abc"}

def test_syntax_error2():
   False = 0
   with pytest.raises(SyntaxError):
       False
