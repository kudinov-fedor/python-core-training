import pytest

from tests.pytest_example.tested_objects import X
from tests.pytest_example import tested_objects


@pytest.mark.foo
@pytest.mark.bar
def test_success():
    assert 1 == 1


@pytest.mark.buzz
@pytest.mark.bar
def test_failure():
    assert 1 == 2


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (1, -1, 0),
    pytest.param(3, 2, 5, marks=pytest.mark.foo)
])
def test_parametrized(a, b, expected):
    assert a + b == expected


def test_mock_method(mocker):
    mocker.patch.object(X, "y", return_value="some")
    assert X().y() == "some"


def test_mock_attribute(mocker):
    # need to patch x attr in instance of X class
    # can not do that straight as 'x' does not exist in X
    # and will appear only during __init__ invocation
    # we can create instance beforehand, setup attrs as expected
    # patch X class, to return x instance on instantination

    x = X()
    x.x = 321
    mocker.patch.object(X, '__new__', return_value=x)
    mocker.patch.object(X, '__init__', return_value=None)  # switch off init

    assert X().x == 321


def test_mock_global_var(monkeypatch):
    monkeypatch.setattr(tested_objects, "GLOBAL_ITEM", 321)
    assert X().return_global_item() == 321


@pytest.mark.skip
def test_skip():
    assert 1 == 1


import os
DEBUG = os.environ.get("DEBUG", True)


@pytest.mark.skipif(condition=DEBUG, reason="Skip if Debug")
def test_skip_if_debug():
    assert 1 == 1


@pytest.mark.xfail
def test_skip_if_fails():
    assert 1 == 0


def test_skip_in_runtime():
    if DEBUG:
        pytest.skip("Skip if Debug")
