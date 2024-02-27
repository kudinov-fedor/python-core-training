class AbstractCook:
    food = "Food"
    drink = "Drink"
    food_total = 0
    drink_total = 0

    def add_food(self, food_amount: int, food_price: int):
        self.food_total += food_amount * food_price

    def add_drink(self, portion_number: int, drink_price: int):
        self.drink_total += portion_number * drink_price

    def total(self):
        total = self.food_total + self.drink_total
        return f"{self.food}: {self.food_total}, {self.drink}: {self.drink_total}, Total: {total}"


class JapaneseCook(AbstractCook):
    food = "Sushi"
    drink = "Tea"


class UkrainianCook(AbstractCook):
    food = "Pampushky"
    drink = "Uzvar"


class ItalianCook(AbstractCook):
    food = "Pizza"
    drink = "Juice"
