import pytest
import random

@pytest.mark.parametrize("input1, input2, expected_max", [
    (4, 5, 5),
    (-1, 0, 0),
    (3, 3, 3)
])
def test_max_value(input1, input2, expected_max):
    assert max(input1, input2) == expected_max


@pytest.fixture
def get_random_list():
    return [random.randint(1,100) for _ in range(5)]


@pytest.mark.xfail(strict=False)
def test_list_sum(get_random_list):
    assert sum(get_random_list) > 200, "Sum of elements is not enough"


@pytest.fixture
def counter():
    yield range(10)

@pytest.mark.parametrize("test_list", [
    ["qwe", "asd", "zxc"],
    ["tested"]
])
def test_enumerator(test_list, counter):
    en_list = list(enumerate(test_list))
    for num, value, numerated_value in zip(counter, test_list, en_list):
        assert (num, value) == numerated_value
