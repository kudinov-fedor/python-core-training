class AbstractCook:
    food_name = "Food"
    drink_name = "Drink"
    food_total = 0
    drink_total = 0

    def add_food(self, count: int, price: int):
        self.food_total += count*price

    def add_drink(self, count: int, price: int):
        self.drink_total += count*price

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

    print(client_1.total())
    print(client_2.total())
    print(client_3.total())

