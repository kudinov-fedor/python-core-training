class AbstractCook:
    def __init__(self):
        self.food_total = 0
        self.drink_total = 0

    def add_food(self, food_amount, food_price):
        total_food_price = food_amount * food_price
        self.food_total += total_food_price

    def add_drink(self, drink_amount, drink_price):
        total_drink_price = drink_amount * drink_price
        self.drink_total += total_drink_price

    def total(self):
        total_food = self.food_total
        total_drink = self.drink_total
        return f"{self.meal}: {total_food}, {self.beverage}: {total_drink}, Total: {total_food + total_drink}"


class JapaneseCook(AbstractCook):
    meal, beverage = 'Sushi', 'Tea'


class FrenchCook(AbstractCook):
    meal, beverage = 'Croissant', 'Coffee'


class ItalianCook(AbstractCook):
    meal, beverage = 'Pizza', 'Juice'


if __name__ == "__main__":
    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = FrenchCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)
    print(client_2.total())
    print(client_1.total())
    print(client_3.total())

    assert client_2.total() == "Croissant: 90, Coffee: 100, Total: 190"
    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
