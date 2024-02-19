from datetime import datetime


class Person:
    PREFIX = {"unknown": "Is",
              "male": "He is",
              "female": "She is"}

    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        now = datetime.now()
        not_full_year = (now.month, now.day) < (self.birth_date.month, self.birth_date.day)
        return now.year - self.birth_date.year - not_full_year

    def work(self):
        return f"{self.PREFIX[self.gender]} a {self.job}"

    def money(self):
        return f"{self.salary * self.working_years*12:_}".replace("_", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"
