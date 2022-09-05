CAR = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


def test_get_existing_value():
    """Get a value for an existing key"""
    assert CAR.get('brand') == CAR['brand']


def test_get_with_default_value_existing():
    """Get a value for an existing key with default"""
    assert CAR.get('brand', 'BMW') == CAR['brand']


def test_get_non_existent_key():
    """Get a value for a non existent key"""
    assert CAR.get('passenger') is None


def test_get_with_default_value_non_existent():
    """Get a value for an existing key with default"""
    assert CAR.get('passenger', 'Anton') == 'Anton'
