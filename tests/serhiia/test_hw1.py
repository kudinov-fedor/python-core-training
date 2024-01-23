

def test_max_value():
    x = max(3, 4, 5)
    assert x == 5

def test_min_value():
    x = min([5, 3, 4])
    assert x == 3

def test_max_string():
    x = max("sfdsdf")
    assert x == 's'

def test_min_value_by_length():
    x = min("banana", "ball", "cat", key=len)
    assert x == "cat"

def test_true_or_false():
    x = [] or "abc"
    assert x == "abc"

def test_true_or_false_blnk():
    x = None or 0 or "" or [] or {}
    assert x == {}

def test_isTuple():
    x = divmod(5, 2)
    assert type(x) == tuple
    assert x == (2, 1)