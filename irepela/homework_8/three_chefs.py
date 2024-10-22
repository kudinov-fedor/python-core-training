# Details:  https://py.checkio.org/mission/3-chefs/share/33d5c11b5ff002a1645a6ee3b93ce00a/


class AbstractCook:

    def __init__(self):
        self.total_food = 0
        self.total_drink = 0

    def add_food(self, food_amount: int, food_price: int):
        self.total_food += food_amount * food_price

    def add_drink(self, drink_amount: int, drink_price: int):
        self.total_drink += drink_amount * drink_price

    def total(self):
        pass


class JapaneseCook(AbstractCook):

    def total(self):
        return f"Sushi: {self.total_food}, Tea: {self.total_drink}, Total: {self.total_food + self.total_drink}"


class UkrainianCook(AbstractCook):

    def total(self):
        return f"Borsch: {self.total_food}, Compote: {self.total_drink}, Total: {self.total_food + self.total_drink}"


class ItalianCook(AbstractCook):

    def total(self):
        return f"Pizza: {self.total_food}, Juice: {self.total_drink}, Total: {self.total_food + self.total_drink}"
