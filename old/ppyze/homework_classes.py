from datetime import datetime
from collections import OrderedDict


class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def __repr__(self):
        return f'Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})'

    @property
    def east(self):
        return self.west + self.width_WE

    @property
    def north(self):
        return self.south + self.width_NS

    def corners(self):
        return {'north-east': [self.north, self.east],
                'south-east': [self.south, self.east],
                'south-west': [self.south, self.west],
                'north-west': [self.north, self.west]}

    def area(self):
        return abs(self.north - self.south) * abs(self.west - self.east)

    def volume(self):
        return self.area() * self.height


class Person:

    PREFIX = {'unknown': 'Is',
              'male': 'He is',
              'female': 'She is'}

    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, '%d.%m.%Y')
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        now = datetime.now()
        not_full_year = (self.birth_date.month, self.birth_date.day) > (now.month, now.day)
        return (now.year - self.birth_date.year) - not_full_year

    def work(self):
        prefix = self.PREFIX[self.gender]
        return f'{prefix} a {self.job}'

    def money(self):
        return f'{self.salary * self.working_years * 12:_}'.replace('_', '' '')

    def home(self):
        return f'Lives in {self.city}, {self.country}'


class AbstractCook:
    menu = {'food': 'Food',
            'drink': 'Drink'}

    def __init__(self):
        self.order = OrderedDict()

    def _add_item(self, key, count, price):
        if key not in self.menu:
            raise ValueError(f' {key} item is not available')

        name = self.menu[key]

        if name not in self.order:
            self.order[name] = 0
        self.order[name] += count * price

    def total(self):
        total_price = 0
        result = []
        for item, price in self.order.items():
            total_price += price
            result.append(f'{item}: {price}')
        result.append(f'Total: {total_price}')
        return ', '.join(result)

    def add_food(self, count: int, price: int):
        self._add_item('food', count, price)

    def add_drink(self, count: int, price: int):
        self._add_item('drink', count, price)


class JapaneseCook(AbstractCook):
    menu = {'food': 'Sushi',
            'drink': 'Tea'}


class RussianCook(AbstractCook):
    menu = {'food': 'Dumplings',
            'drink': 'Compote'}


class ItalianCook(AbstractCook):
    menu = {'food': 'Pizza',
            'drink': 'Juice'}


class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0

    def perform_attack(self, warrior: 'Warrior'):
        warrior.receive_dmg(self.attack)

    def receive_dmg(self, damage: int):
        self.health = max(0, self.health - damage)


class Knight(Warrior):
    attack = 7


def fight(unit_1: Warrior, unit_2: Warrior):
    while unit_1.is_alive:
        unit_1.perform_attack(unit_2)
        if not unit_2.is_alive:
            break
        unit_2.perform_attack(unit_1)
    return unit_1.is_alive
