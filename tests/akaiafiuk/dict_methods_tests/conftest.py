import pytest


@pytest.fixture()
def default_dict():
    return {1: 'one', 2: 'two', 3: 'three'}