# Details:  https://py.checkio.org/mission/3-chefs/share/33d5c11b5ff002a1645a6ee3b93ce00a/


class AbstractCook:

    def __init__(self):
        self.total_food = 0
        self.total_drink = 0
        self.labels = {
            "food": "Food",
            "drink": "Drink"
        }

    def add_food(self, food_amount: int, food_price: int):
        self.total_food += food_amount * food_price

    def add_drink(self, drink_amount: int, drink_price: int):
        self.total_drink += drink_amount * drink_price

    def total(self):
        return (f"{self.labels["food"]}: {self.total_food}, "
                f"{self.labels["drink"]}: {self.total_drink}, "
                f"Total: {self.total_food + self.total_drink}")


class JapaneseCook(AbstractCook):

    def __init__(self):
        super().__init__()
        self.labels = {
            "food": "Sushi",
            "drink": "Tea"
        }


class UkrainianCook(AbstractCook):

    def __init__(self):
        super().__init__()
        self.labels = {
            "food": "Borsch",
            "drink": "Compote"
        }


class ItalianCook(AbstractCook):

    def __init__(self):
        super().__init__()
        self.labels = {
            "food": "Pizza",
            "drink": "Juice"
        }
