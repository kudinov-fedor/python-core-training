
class AbstractCook:
    food_total = 0
    drink_total = 0

    def __init__(self, food_name: str, drink_name: str):
        self.menu = {'food': food_name, 'drink': drink_name}

    def add_food(self, food_amount: int, food_price: int):
        self.food_total += food_amount * food_price

    def add_drink(self, portion_number: int, drink_price: int):
        self.drink_total += portion_number * drink_price

    def total(self):
        total = self.food_total +self.drink_total
        return f"{self.menu['food']}: {self.food_total}, {self.menu['drink']}: {self.drink_total}, Total: {total}"


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__('Sushi', 'Tea')


class UkrainianCook(AbstractCook):
    def __init__(self):
        super().__init__('Pampushky', 'Uzvar')


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__('Pizza', 'Juice')
