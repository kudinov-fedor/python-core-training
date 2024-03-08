from nataliia_romanchuk.homework_8.three_chefs import JapaneseCook, UkrainianCook, ItalianCook


def test_jap():
    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)
    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"


def test_ukr():
    client_2 = UkrainianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)
    assert client_2.total() == "Pampushky: 90, Uzvar: 100, Total: 190"


def test_italy():
    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
