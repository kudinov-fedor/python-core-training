class AbstractCook:
    meal = None
    drink = None

    def __init__(self, food_amount=0, drink_amount=0):  # default values
        self.food_amount = food_amount
        self.drink_amount = drink_amount

    def add_food(self, food_amount, food_price):
        self.food_amount += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.drink_amount += drink_amount * drink_price

    def total(self):
        return f"{self.meal}: {self.food_amount}, {self.drink}: {self.drink_amount}, Total: {self.food_amount + self.drink_amount}"


class JapaneseCook(AbstractCook):
    meal = 'Sushi'
    drink = 'Tea'


class UkrainianCook(AbstractCook):
    meal = 'Dumplings'
    drink = 'Compote'


class ItalianCook(AbstractCook):
    meal = 'Pizza'
    drink = 'Juice'
