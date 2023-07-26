import pytest

from olpopova.homework.homework08.chiefs import JapaneseCook, UkrainianCook, ItalianCook


@pytest.mark.parametrize(['cuisine', 'first_order', 'second_order', 'drinks', 'expected'], [
    (JapaneseCook(), (2, 30), (3, 15), (2, 10), 'Sushi: 105, Tea: 20, Total: 125'),
    (UkrainianCook(), (1, 40), (2, 25), (5, 20),"Borsch: 90, Uzvar: 100, Total: 190"),
    (ItalianCook(), (2, 20), (2, 30), (2, 10), "Spaghetti: 100, Wine: 20, Total: 120")
])
def test_receipt(cuisine, first_order, second_order, drinks, expected):
    client = cuisine
    client.add_food(*first_order)
    client.add_food(*second_order)
    client.add_drink(*drinks)
    assert client.total() == expected, 'Incorrect actual values'
