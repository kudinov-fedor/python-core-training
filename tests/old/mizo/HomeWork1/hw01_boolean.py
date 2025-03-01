# if at least one is true

def test_any_function():
    assert any(["", 0, False, (1,), None]) is True
