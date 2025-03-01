
class AbstractCook:

    food = 0
    drinks = 0
    food_name = 'Food'
    drink_name = 'Drink'

    def add_food(self, food, price):
        self.food += food * price

    def add_drink(self, drinks, price):
        self.drinks += drinks * price

    def total_sum(self):
        return self.food + self.drinks

    def total(self):
        return f'{self.food_name}: {self.food}, {self.drink_name}: {self.drinks}, Total: {self.total_sum()}'


class JapaneseCook(AbstractCook):
    food_name = 'Sushi'
    drink_name = 'Tea'


class UkrainianCook(AbstractCook):
    food_name = 'Borsch'
    drink_name = 'Uzvar'


class ItalianCook(AbstractCook):
    food_name = 'Pizza'
    drink_name = 'Juice'
