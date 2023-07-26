
class AbstractCook:

    food = 0
    drinks = 0

    def add_food(self, food, price):
        self.__setattr__('food', self.food + food * price)

    def add_drink(self, drinks, price):
        self.__setattr__('drinks', self.drinks + drinks * price)

    def total_sum(self):
        return self.food + self.drinks

    def total(self):
        pass


class JapaneseCook(AbstractCook):
    def total(self):
        return f'Sushi: {self.food}, Tea: {self.drinks}, Total: {self.total_sum()}'


class UkrainianCook(AbstractCook):
    def total(self):
        return f'Borsch: {self.food}, Uzvar: {self.drinks}, Total: {self.total_sum()}'


class ItalianCook(AbstractCook):
    def total(self):
        return f'Spaghetti: {self.food}, Wine: {self.drinks}, Total: {self.total_sum()}'
