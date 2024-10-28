import pytest
from tkupchyn.homework_08.three_chefs import (AbstractCook, ItalianCook, UkrainianCook, JapaneseCook)


@pytest.mark.parametrize('client, food, drinks, total',
                         (
                                 (JapaneseCook(),
                                  {'first_food': (2, 30), 'second_food': (3, 15)},
                                  {'first_drink': (2, 10), 'second_drink': (4, 5)},
                                  'Sushi: 105, Tea: 40, Total: 145'),

                                 (UkrainianCook(),
                                  {'first_food': (5, 25), 'second_food': (3, 15)},
                                  {'first_drink': (3, 8), 'second_drink': (1, 5)},
                                  'Varenyky: 170, Uzvar: 29, Total: 199'),


                                 (ItalianCook(),
                                  {'first_food': (5, 16), 'second_food': (2, 10)},
                                  {'first_drink': (5, 8), 'second_drink': (3, 3)},
                                  'Pizza: 100, Juice: 49, Total: 149'),

                                 (AbstractCook(),
                                  {'first_food': (1, 1), 'second_food': (1, 1)},
                                  {'first_drink': (2, 2), 'second_drink': (2, 2)},
                                  'Food: 2, Drinks: 8, Total: 10')
                         ))
def test_chefs(client, food, drinks, total):
    client.add_drink(*drinks['first_drink'])
    client.add_drink(*drinks['second_drink'])
    client.add_food(*food['first_food'])
    client.add_food(*food['second_food'])

    assert client.total() == total
