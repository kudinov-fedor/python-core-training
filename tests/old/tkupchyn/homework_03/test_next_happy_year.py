import pytest
from old.tkupchyn.homework_03.next_happy_year import next_happy_year, next_happy_year_alternative


@pytest.mark.parametrize("current_year, happy_year",
                         [
                             (7712, 7801),
                             (8989, 9012),
                             (1001, 1023),
                             (1987, 2013)
                         ])
def test_next_happy_year(current_year, happy_year):
    assert next_happy_year(current_year) == happy_year


@pytest.mark.parametrize("current_year, happy_year",
                         [
                             (7712, 7801),
                             (8989, 9012),
                             (1001, 1023),
                             (1987, 2013)
                         ])
def test_next_happy_year_alternative(current_year, happy_year):
    assert next_happy_year_alternative(current_year) == happy_year
