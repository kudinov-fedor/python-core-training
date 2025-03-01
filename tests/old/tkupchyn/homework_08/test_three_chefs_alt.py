import pytest
from tkupchyn.homework_08.three_chefs_alt import (AbstractCook, ItalianCook, UkrainianCook, JapaneseCook)


@pytest.mark.parametrize("cook, orders, expected_result",
                         [(AbstractCook,
                           [('Food', 2, 13), ('fooD', 5), ('drink', 4)],
                           "Food: 151, Drink: 124, Total:275"),

                          (UkrainianCook,
                           [('Varenyky', 2, 13), ('borsch', 10, 35), ('varenyky', 4), ('uzvar', 4, 15)],
                           "Varenyky: 306, Borsch: 350, Uzvar: 60, Total:716"),

                          (ItalianCook,
                           [('Pizza', 2, 10), ('pizza', 10), ('juice', 5)],
                           "Pizza: 320, Juice: 50, Total:370"),

                          (JapaneseCook,
                           [('Sushi', 3, 20), ('tea', 1)],
                           "Sushi: 60, Tea: 20, Total:80"),

                          ])
def test_cook(cook, orders, expected_result):
    cook = cook()
    for order in orders:
        cook.add_to_order(*order)
    assert cook.total() == expected_result
