from collections import OrderedDict
from functools import partialmethod


class Restaurant:
    menu = {'first_course': 'First Course',
            'second_course': 'Second Course',
            'dessert': 'Dessert',
            'beverage': 'Beverage'}

    def __init__(self):
        self.order = OrderedDict()

    def _add_item(self, key, count, price):
        if key not in self.menu:
            raise ValueError(f'{key} is not available in the menu')

        name = self.menu[key]

        if name not in self.order:
            self.order[name] = 0
        self.order[name] += count * price

    add_first_course = partialmethod(_add_item, "first_course")
    add_second_course = partialmethod(_add_item, "second_course")
    add_dessert = partialmethod(_add_item, "dessert")
    add_beverage = partialmethod(_add_item, "beverage")

    def calculate_total_cost(self):
        total_cost = 0
        result = []
        for item, price in self.order.items():
            total_cost += price
            result.append(f"{item}: {price}")
        result.append(f"Total cost: {total_cost}")

        return ", ".join(result)


class ItalianRestaurant(Restaurant):
    menu = {'first_course': 'Pasta',
            'second_course': 'Potato with chicken',
            'dessert': 'Tiramisu',
            'beverage': 'Sparkling water'}


class SpanishRestaurant(Restaurant):
    menu = {'first_course': 'Seafood soup',
            'second_course': 'Paella with seafood',
            'dessert': 'Banana mousse',
            'beverage': 'Juice'}


def get_client_order(menu, first, second, desert, beverages):
    menu.add_first_course(first[0], first[1])
    menu.add_second_course(second[0], second[1])
    menu.add_dessert(desert[0], desert[1])
    menu.add_beverage(beverages[0], beverages[1])


if __name__ == '__main__':
    menu1 = ItalianRestaurant()
    menu2 = SpanishRestaurant()

    get_client_order(menu1, (2, 10), (2, 20), (2, 15), (4, 3))
    get_client_order(menu2, (2, 8), (2, 25), (2, 10), (4, 5))

    assert menu1.calculate_total_cost() == ('Pasta: 20, Potato with chicken: 40, Tiramisu: 30, '
                                            'Sparkling water: 12, Total cost: 102')
    assert menu2.calculate_total_cost() == ('Seafood soup: 16, Paella with seafood: 50, Banana mousse: 20, '
                                            'Juice: 20, Total cost: 106')
