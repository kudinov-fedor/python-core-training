# Details:  https://py.checkio.org/mission/every-person-is-unique/share/1c6fd4b663f7e40fa15b699f17efab40/
from datetime import datetime
from math import floor


class Person:

    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city,
                 gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        current_date = datetime.strptime("01.01.2018", "%d.%m.%Y")
        birth_date = datetime.strptime(self.birth_date, "%d.%m.%Y")
        age = floor((current_date - birth_date).days / 365)
        return age

    def work(self):
        if self.gender == "male":
            prefix = "He is a"
        elif self.gender == "female":
            prefix = "She is a"
        else:
            prefix = "Is a"
        return f"{prefix} {self.job}"

    def money(self):
        calculated_salary = self.working_years * self.salary * 12
        return '{:,}'.format(calculated_salary).replace(',', ' ')

    def home(self):
        return f"Lives in {self.city}, {self.country}"
