import pytest

from ihontaryk.homework_10.context_manager_try_except import Catcher, divide_numbers


@pytest.mark.parametrize('arguments',
                         [(1, 0, False),
                          (-1, 0, ZeroDivisionError, False),
                          (-1, 0, (TypeError, ZeroDivisionError), False),
                          (1, 1, None, True),
                          ])
def test_catcher(arguments):
    """
    verify catcher context manager
    """

    num1, num2, *errors, expected_result = arguments

    with Catcher(*errors):
        result = divide_numbers(num1, num2)

        assert result == expected_result
