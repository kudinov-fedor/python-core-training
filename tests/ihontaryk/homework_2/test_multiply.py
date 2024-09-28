import pytest

from ihontaryk.homework_2.multiply import multiply_numbers


@pytest.mark.parametrize('number1, number2,  expected_result',
                         [(0, 2, 0),
                          (2, 5, 10),
                          (-5, -5, 25),
                          (-55.5, 2, -111.0),
                          (False, 1, 0),
                          (5, True, 5)
                          ])
def test_multiply_numbers_positive(number1, number2, expected_result):
    """
    verify positive scenarios for multiply_numbers function
    """
    assert multiply_numbers(number1, number2) == expected_result


@pytest.mark.parametrize('number1, number2,  error',
                         [('abc', 2, TypeError),
                          ((False,), 1, TypeError),
                          (4, [1, 2, 3], TypeError),
                          (8, {1, 2, 3}, TypeError)
                          ])
def test_multiply_numbers_negative(number1, number2, error):
    """
    verify negative scenarios for multiply_numbers function
    """
    with pytest.raises(error):
        multiply_numbers(number1, number2)

