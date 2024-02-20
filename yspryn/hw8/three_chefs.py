class AbstractCook:

    def __init__(self):
        self.drink = ""
        self.food = ""
        self.food_order = []
        self.drink_order = []

    def add_food(self, food_count, food_price):
        self.food_order.append((food_count, food_price))

    def add_drink(self, drink_count, drink_price):
        self.drink_order.append((drink_count, drink_price))

    def total(self):
        total_food = 0
        for item, price in self.food_order:
            total_food += item * price
        total_drink = 0
        for item, price in self.drink_order:
            total_drink += item * price
        return f"{self.food}: {total_food}, {self.drink}: {total_drink}, Total: {total_drink + total_food}"


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food = "Sushi"
        self.drink = "Tea"


class UkrainianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.drink = "Compote"
        self.food = "Dumplings"


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.drink = "Juice"
        self.food = "Pizza"
