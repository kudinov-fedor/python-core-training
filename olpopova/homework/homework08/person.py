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
        separator = self.birth[2]
        return date.today().year - datetime.strptime(self.birth, f'%d{separator}%m{separator}%Y').year

    def work(self):
        return f'{self.fn} is a {self.job}'

    def money(self):
        return ' '.join([f'Earned in {self.work_years} years -',
                         '{0:,}'.format(self.salary * 12 * self.work_years).replace(',', ' ')])

    def home(self):
        return f'Lives in {self.city}, {self.country}'
