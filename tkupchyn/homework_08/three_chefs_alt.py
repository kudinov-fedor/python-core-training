# Details:  https://py.checkio.org/mission/3-chefs/share/33d5c11b5ff002a1645a6ee3b93ce00a/
from collections import defaultdict


class AbstractCook:
    menu = {'food': 25,
            'drink': 31}

    def __init__(self):
        self.order = defaultdict(int)

    def total(self):
        total = ''
        total_sum = 0
        for k, v in self.order.items():
            total += f'{k.capitalize()}: {v}, '
            total_sum += v
        total += f'Total:{total_sum}'
        return total

    def add_to_order(self, name, amount, price=None):
        name = name.lower()
        price = price or self.menu[name]
        if name in self.menu:
            self.order[name] += amount * price
        else:
            raise ValueError(' This item is not in menu')


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.menu = {'sushi': 56,
                     'tea': 20}


class UkrainianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.menu = {'varenyky': 70,
                     'borsch': 65,
                     'uzvar': 15}


class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__()
        self.menu = {'pizza': 30,
                     'juice': 10}
