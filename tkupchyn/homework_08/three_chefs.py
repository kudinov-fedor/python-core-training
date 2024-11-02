# Details:  https://py.checkio.org/mission/3-chefs/share/33d5c11b5ff002a1645a6ee3b93ce00a/


class AbstractCook:
    total_food = 0
    total_drinks = 0
    food_name = 'Food'
    drink_name = 'Drinks'

    def total(self):
        return (f'{self.food_name}: {self.total_food},'
                f' {self.drink_name}: {self.total_drinks},'
                f' Total: {self.total_food + self.total_drinks}')

    def add_food(self, food_amount, food_price):
        self.total_food += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.total_drinks += drink_amount * drink_price


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food_name = 'Sushi'
        self.drink_name = 'Tea'


class UkrainianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food_name = 'Varenyky'
        self.drink_name = 'Uzvar'


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.food_name = 'Pizza'
        self.drink_name = 'Juice'
