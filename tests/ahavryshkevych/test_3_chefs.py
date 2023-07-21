from ahavryshkevych.task_hw8_3_chefs import JapaneseCook, UkrainianCook, ItalianCook


def test_japanese_cook():
    client = JapaneseCook()
    client.add_food(2, 30)
    client.add_food(3, 15)
    client.add_drink(2, 10)

    assert client.total() == "Sushi: 105, Tea: 20, Total: 125"


def test_ukrainian_cook():
    client = UkrainianCook()
    client.add_food(1, 40)
    client.add_food(2, 25)
    client.add_drink(5, 20)

    assert client.total() == "Dumplings: 90, Compote: 100, Total: 190"


def test_italian_cook():
    client = ItalianCook()
    client.add_food(2, 20)
    client.add_food(2, 30)
    client.add_drink(2, 10)

    assert client.total() == "Pizza: 100, Juice: 20, Total: 120"
