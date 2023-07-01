def test_zip():
    assert list(zip("qwerty", {1, 2, 3, 4})) == [('q', 1), ('w', 2), ('e', 3), ('r', 4)]


def test_dict_items():
    assert list(dict(brand="Ford", model="Mustang", year=1964).items()) == [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]
    assert list({"brand": "Mercedes", "model": "S"}.items()) == [('brand', 'Mercedes'), ('model', 'S')]


def test_enumerate():
    assert list(enumerate(["a", "b", "c"], start=1)) == [(1, "a"), (2, "b"), (3, "c")]
