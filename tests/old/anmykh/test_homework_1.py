import pytest


@pytest.mark.parametrize(["item", "data_type"], [
    ("sad", str)
])
def test_is_string(item, data_type):
    assert isinstance(item, data_type)


@pytest.mark.parametrize(["item", "data_type"],
                         [({3, 2, "sad"}, set)])
def test_is_set(item, data_type):
    assert isinstance(item, data_type)

