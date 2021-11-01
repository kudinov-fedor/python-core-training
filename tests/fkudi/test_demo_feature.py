import pytest

from fkudi.demo_task import demo_feature, demo_division


def test_demo_feature():
    """
    Simple test
    """
    res = demo_feature()
    assert res == 1


@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (5, 2, 2.5),
    (-4, 2, -2),
    (0, 5, 0)
])
def test_division_success(a, b, expected):
    """
    data driven test
    """
    assert demo_division(a, b) == expected


def test_division_error():
    """
    test that error raises
    """
    with pytest.raises(ZeroDivisionError):
        demo_division(5, 0)


def test_demo_mock(mocker):
    mock = mocker.MagicMock()
    len(mock)
    assert mock.__len__.called
