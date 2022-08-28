from collections import OrderedDict
from functools import partialmethod


class AbstractCook:

    menu = {"food": "Food",
            "drink": "Drink"}

    def __init__(self):
        self.order = OrderedDict()

    def _add_item(self, key, count, price):
        """
        Universal method, which can be used to order any items from menu,
        if key is present in menu.
        Adds ordered item to Order structure, in the same order, how orders arrive.
        """
        if key not in self.menu:
            raise ValueError("'{}' menu item is not available".format(key))

        name = self.menu[key]

        if name not in self.order:
            self.order[name] = 0
        self.order[name] += count * price

    def total(self):
        """
        Prepare total from items collected in Order
        """

        total_price = 0
        result = []
        for item, price in self.order.items():
            total_price += price
            result.append(f"{item}: {price}")
        result.append(f"Total: {total_price}")
        return ", ".join(result)

    def add_food(self, count: int, price: int):
        self._add_item("food", count, price)

    def add_drink(self, count: int, price: int):
        self._add_item("drink", count, price)

    # add_food, add_drink can be replaced by:
    # add_food = partialmethod(_add_item, "food")
    # add_drink = partialmethod(_add_item, "drink")


class JapaneseCook(AbstractCook):
    menu = {"food": "Sushi",
            "drink": "Tea"}


class RussianCook(AbstractCook):
    menu = {"food": "Dumplings",
            "drink": "Compote"}


class ItalianCook(AbstractCook):
    menu = {"food": "Pizza",
            "drink": "Juice"}


if __name__ == '__main__':

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125", client_1.total()
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
