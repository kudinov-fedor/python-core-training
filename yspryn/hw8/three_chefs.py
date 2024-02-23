class AbstractCook:
    drink = "Drink"
    food = "Food"

    def __init__(self):
        self.food_order = []
        self.drink_order = []

    def add_food(self, food_count, food_price):
        self.food_order.append((food_count, food_price))

    def add_drink(self, drink_count, drink_price):
        self.drink_order.append((drink_count, drink_price))

    def total(self):
        total_food = sum([item * price for item, price in self.food_order])
        total_drink = sum([item * price for item, price in self.drink_order])
        return f"{self.food}: {total_food}, {self.drink}: {total_drink}, Total: {total_drink + total_food}"


class JapaneseCook(AbstractCook):
    food = "Sushi"
    drink = "Tea"

    def __init__(self):
        super().__init__()


class UkrainianCook(AbstractCook):
    drink = "Compote"
    food = "Dumplings"

    def __init__(self):
        super().__init__()


class ItalianCook(AbstractCook):
    drink = "Juice"
    food = "Pizza"

    def __init__(self):
        super().__init__()
