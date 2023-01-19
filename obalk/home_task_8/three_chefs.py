"""https://py.checkio.org/en/mission/3-chefs"""
from abc import ABC


class AbstractCook(ABC):

    def __init__(self):
        self.food = 0
        self.drink = 0

    def add_food(self, food_amount, food_price):
        self.food += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.drink += drink_amount * drink_price

    def total(self):
        # this part can be and should be moved to tests
        if "food" not in self.MENU:
            raise KeyError("You should have 'food' key in a MENU dict in your Cook")
        if "drink" not in self.MENU:
            raise KeyError("You should have 'drink' key in a MENU dict in your Cook")

        return f"{self.MENU['food']}: {self.food}, {self.MENU['drink']}: {self.drink}, Total: {self.food + self.drink}"

    # this part can be and should be moved to tests
    def __getattr__(self, item):
        if item == "MENU":
            raise AttributeError("You should have MENU it your Cook")


class JapaneseCook(AbstractCook):
    MENU = {"food": "Sushi", "drink": "Tea"}


class KazakhstanCook(AbstractCook):
    MENU = {"food": "Beshbarmak", "drink": "Kumys"}


class ItalianCook(AbstractCook):
    MENU = {"food": "Pizza", "drink": "Juice"}


if __name__ == '__main__':
    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = KazakhstanCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Beshbarmak: 90, Kumys: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
