import pytest
import random

LIST_LEN = 10


@pytest.mark.smoke
def test_assert_in():
    assert 5 in [5, 6, 7]


@pytest.mark.parametrize("test_data1, test_data2, expected", [
    ([1, 2, 3], [56], [1, 2, 3, 56]),
    (1, 7, 8),
    ("test_", "data", "test_data")
])
def test_sum(test_data1, test_data2, expected):
    result = test_data1 + test_data2
    assert result == expected


@pytest.fixture
def pop_list():
    r = random.sample(range(0, 100), LIST_LEN)
    return r


@pytest.mark.smoke
def test_len_list(pop_list):
    assert len(pop_list) == LIST_LEN


@pytest.mark.xfail
def test_append_list_fail():
    assert [1, 2] + 'f'
