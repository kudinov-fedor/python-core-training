import pytest


@pytest.fixture()
def default_dict():
    return {1: 'one', 2: 'two', 3: 'three'}


@pytest.fixture()
def car():
    return {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
