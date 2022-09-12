def test_setdefault_existing_key(car):
    """Setdefault returns an object of a value if key exists"""
    assert car.setdefault("brand", "BMW") == "Ford"


def test_setdefault_does_not_change_existing_item(car):
    """Setdefault does not change an existing value"""
    car.setdefault("brand", "BMW")
    assert car["brand"] == "Ford"


def test_setdefault_non_existent_key(car):
    """Setdefault adds key: value pair if key does not exist and returns value object"""
    assert "driver" not in car
    assert car.setdefault("driver", "Anton") == "Anton"
    assert "driver" in car
    assert car["driver"] == "Anton"


def test_add_kv_and_update_value_using_setdefault(car):
    """Can add a k: v pair and update v in just one string"""
    assert "driver" not in car
    car.setdefault("driver", []).append('Anton')
    assert car["driver"] == ['Anton']


def test_check_default_value(car):
    """Can add a k: v pair and update v in just one string"""
    assert "driver" not in car
    car.setdefault("driver", []).append('Anton')
    assert car["driver"] == ['Anton']