import pytest

from ihontaryk.homework_2.sum_numbers import sum_numbers


@pytest.mark.parametrize('text, expected_result',
                         [('1 2 3 4 5', 15),
                          ('This text is without any number', 0),
                          ('Today is 27.09.2024. Yesterday was 26th of September. 27 is greater than 26', 53)
                          ])
def test_sum_numbers_positive(text, expected_result):
    """
    verify positive scenarios for sum_numbers function
    """

    assert sum_numbers(text) == expected_result


@pytest.mark.parametrize('text, error',
                         [(123, TypeError),
                          (100.0, TypeError),
                          (['abc'], TypeError),
                          ({'This text is without any number'}, TypeError),
                          ({'Number': 5}, TypeError),
                          ('', ValueError)
                          ])
def test_sum_numbers_negative(text, error):
    """
    verify negative scenarios for sum_numbers function
    """

    with pytest.raises(error):
        sum_numbers(text)
