"""https://py.checkio.org/en/mission/3-chefs"""
from abc import ABC
from collections import defaultdict
import functools


class AbstractCook(ABC):
    AVAILABLE_CATEGORIES = ["food", "drink", "snack", "soup"]

    def __init__(self):
        self.order: dict = defaultdict(int)

    def _add_menu_item(self, menu_type: str, count: int, price: int):
        """
        Universal method, which can be used to order any items from menu,
        if key is present in menu.
        Adds ordered item to Order structure, in the same order, how orders arrive.
        """
        if menu_type not in self.AVAILABLE_CATEGORIES:
            raise ValueError(f"'{menu_type.capitalize()}' option is unavailable for Cooker")
        if menu_type not in self.MENU:
            raise ValueError(f"Cooker doesn't have '{menu_type}' in his menu")
        name = self.MENU[menu_type]

        self.order[name] += count * price

    add_food: "functools.partialmethod" = functools.partialmethod(_add_menu_item, menu_type="food")
    add_drink: "functools.partialmethod" = functools.partialmethod(_add_menu_item, menu_type="drink")
    add_soup: "functools.partialmethod" = functools.partialmethod(_add_menu_item, menu_type="soup")

    def total(self):
        """
        Prepare total from items collected in Order
        """

        total_price = 0
        result = []
        for menu_item, price in self.order.items():
            total_price += price
            result.append(f"{menu_item}: {price}")
        result.append(f"Total: {total_price}")
        return ", ".join(result)

    def __getattr__(self, item):
        if item == "MENU":
            raise AttributeError("You should have MENU it your Cook")


class JapaneseCook(AbstractCook):
    MENU = {"food": "Sushi", "drink": "Tea"}


class KazakhstanCook(AbstractCook):
    MENU = {"food": "Beshbarmak", "drink": "Kumys"}


class ItalianCook(AbstractCook):
    MENU = {"food": "Pizza", "drink": "Juice", "soup": "Minestrone"}


if __name__ == '__main__':
    client_1 = JapaneseCook()
    client_1.add_food(count=2, price=30)
    client_1.add_food(count=3, price=15)
    client_1.add_drink(count=2, price=10)

    client_2 = KazakhstanCook()
    client_2.add_food(count=1, price=40)
    client_2.add_food(count=2, price=25)
    client_2.add_drink(count=5, price=20)

    client_3 = ItalianCook()
    client_3.add_food(count=2, price=20)
    client_3.add_food(count=2, price=30)
    client_3.add_drink(count=2, price=10)
    client_3.add_soup(count=2, price=15)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Beshbarmak: 90, Kumys: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Minestrone: 30, Total: 150"
