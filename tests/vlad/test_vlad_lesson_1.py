import pytest


@pytest.mark.smoke
def test_assert_in():
    assert 5 in [5, 6, 7]


@pytest.mark.parametrize("value, expected", [
    ([1, 2, 3], 3),
    ([1, "asdf", None], 3),
    ("qwerty", 6),
    (set(), 0)
])
def test_len_positive(value, expected):
    assert len(value) == expected


@pytest.mark.xfail
def test_append_list_fail():
    assert [1, 2, 3] + 'str'


@pytest.mark.smoke
def test_sum1(mocker):
    mocker.patch(__name__ + ".sum", return_value=9)
    assert sum(2, 3) != 5
    assert sum(2, 3) == 9


@pytest.mark.smoke
def test_sum2(mocker):
    def crazy_sum(a, b):
      return b + b

    mocker.patch(__name__ + ".sum", side_effect=crazy_sum)
    assert sum(2, 3) == 6
