
class AbstractCook:
    def __init__(self):
        self.food_total = 0
        self.drink_total = 0

    def add_food(self, food_amount, food_price):
        self.food_total = self.food_total + food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.drink_total = self.drink_total + drink_amount * drink_price

    def total(self):
        return f"{self.food_name}: {self.food_total}, {self.drink_name}: {self.drink_total}, Total: " \
               f"{self.food_total + self.drink_total}"


class JapaneseCook(AbstractCook):
    food_name = "Sushi"
    drink_name = "Tea"


class RussianCook(AbstractCook):
    food_name = "Dumplings"
    drink_name = "Compote"


class ItalianCook(AbstractCook):
    food_name = "Pizza"
    drink_name = "Juice"


if __name__ == '__main__':

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125", client_1.total()
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
