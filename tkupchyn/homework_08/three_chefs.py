# Details:  https://py.checkio.org/mission/3-chefs/share/33d5c11b5ff002a1645a6ee3b93ce00a/


class AbstractCook:

    def __init__(self):

        self.total_food = 0
        self.total_drinks = 0
        self.food_name = 'Food'
        self.drink_name = 'Drinks'

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


client = AbstractCook()
client.add_food(23, 5)
print(client.total_food, client.total_drinks, client.total())

client.add_food(53, 10)
print(client.total_food, client.total_drinks, client.total())

if __name__ == '__main__':

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = UkrainianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)
    print(client_2.total())
    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125", client_1.total()
    assert client_2.total() == "Varenyky: 90, Uzvar: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
