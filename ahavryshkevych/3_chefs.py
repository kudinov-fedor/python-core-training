class AbstractCook:
    def __init__(self, food_name, drink_name):
        self.food = 0
        self.drink = 0
        self.food_name = food_name
        self.drink_name = drink_name

    def add_food(self, food_amount, food_price):
        total_cost = food_amount * food_price
        self.food += total_cost


    def add_drink(self, drink_amount, drink_price):
        total_cost = drink_amount * drink_price
        self.drink += total_cost



    def total(self):
        return f"{self.food_name}: {self.food}, {self.drink_name}: {self.drink}, Total: {self.food + self.drink}"




class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__(food_name="Sushi", drink_name="Tea")



class UkrainianCook(AbstractCook):
    def __init__(self):
        super().__init__(food_name="Dumplings", drink_name="Compote")


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__(food_name="Pizza", drink_name="Juice")



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


    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125", client_1.total()
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
