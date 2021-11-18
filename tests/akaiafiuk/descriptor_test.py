import pytest

from akaiafiuk.descriptor_test_drive import Car as DescriptorCar
from akaiafiuk.property_test_drive import Car as PropertyCar
from akaiafiuk.property_outside_class import Car as PropertyOutsideCar


@pytest.mark.parametrize("func", [
    DescriptorCar,
    PropertyCar,
    PropertyOutsideCar
])
def test_valid_car(func):
    bmw = func("BMW", "M3", 360)
    assert str(bmw) == "Make: BMW, Model: M3, Maximum Speed: 360"


@pytest.mark.parametrize("func", [
    DescriptorCar,
    PropertyCar,
    PropertyOutsideCar
])
def test_car_after_speed_update(func):
    bmw = func("BMW", "M3", 360)
    bmw.max_speed = 400
    assert str(bmw) == "Make: BMW, Model: M3, Maximum Speed: 400"


@pytest.mark.parametrize("func", [
    DescriptorCar,
    PropertyCar,
    PropertyOutsideCar
])
def test_value_error(func):
    with pytest.raises(ValueError):
        func("BMW", "M3", -360)


@pytest.mark.parametrize("func", [
    DescriptorCar,
    PropertyCar,
    PropertyOutsideCar
])
def test_type_error(func):
    with pytest.raises(TypeError):
        func("BMW", "M3", "360")
