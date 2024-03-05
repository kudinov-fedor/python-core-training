class AbstractCook:
    food_name = "Food"
    drink_name = "Drink"
    food_total = 0
    drink_total = 0

    def add_food(self, count: int, price: int):
        self.food_total += count * price

    def add_drink(self, count: int, price: int):
        self.drink_total += count * price

    def total(self):
        return (f"{self.food_name}: {self.food_total}, {self.drink_name}: {self.drink_total}, "
                f"Total: {self.food_total + self.drink_total}")


class JapaneseCook(AbstractCook):
    food_name = "Sushi"
    drink_name = "Tea"


class UkrainianCook(AbstractCook):
    food_name = "Borsch"
    drink_name = "Compote"


class ItalianCook(AbstractCook):
    food_name = "Pizza"
    drink_name = "Juice"
