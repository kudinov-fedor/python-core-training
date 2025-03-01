import pytest
from ppyze.main_1 import check_python_operator_and, check_python_operator_or


@pytest.mark.parametrize('var_1, var_2, expected', [
    (True, False, False),
    (True, 0, 0),
    (False, 1, False),
    ('abc', '', '')
])
def test_check_python_operator_and(var_1, var_2, expected):
    """
    data driven test
    """
    assert check_python_operator_and(var_1, var_2) == expected


@pytest.mark.parametrize('var_1, var_2, expected', [
    (True, False, True),
    (True, 0, True),
    (False, 1, 1),
    ('abc', '', 'abc'),
    ('ABC', True, 'ABC')
])
def test_check_python_operator_or(var_1, var_2, expected):
    """
    data driven test
    """
    assert check_python_operator_or(var_1, var_2) == expected
