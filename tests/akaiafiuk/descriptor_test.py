import pytest

from akaiafiuk.descriptor_test_drive import Car


def test_valid_car():
    bmw = Car("BMW", "M3", 360)
    assert str(bmw) == "Make: BMW, Model: M3, Maximum Speed: 360"


def test_car_after_speed_update():
    bmw = Car("BMW", "M3", 360)
    bmw.max_speed = 400
    assert str(bmw) == "Make: BMW, Model: M3, Maximum Speed: 400"


def test_value_error():
    with pytest.raises(ValueError):
        Car("BMW", "M3", -360)


def test_type_error():
    with pytest.raises(TypeError):
        Car("BMW", "M3", "360")
