import datetime
from datetime import date, datetime


class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.fn = first_name
        self.ln = last_name
        self.birth = birth_date
        self.job = job
        self.work_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return ' '.join([self.fn, self.ln])

    def age(self):
        return date.today().year - self.birth.year

    def work(self):
        return f'Is a {self.job}'

    def money(self):
        money = '{0:,}'.format(self.salary * 12 * self.work_years).replace(',', ' ')
        return money

    def home(self):
        return f'Lives in {self.city}, {self.country}'
