import pytest
import hw9_remember_class


@pytest.fixture
def mazda_car():
    return hw9_remember_class.Cars("Mazda", "Cx-5")


@pytest.fixture
def toyota_car():
    return hw9_remember_class.Cars("Toyota", "Highlander")


def test_check_usage(mazda_car, toyota_car):
    all_instances = hw9_remember_class.RememberObject.get_all_instances()
    assert len(all_instances) == 4
