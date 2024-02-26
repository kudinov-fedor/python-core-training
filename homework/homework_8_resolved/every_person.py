from datetime import datetime

CURRENT_DATE = datetime(2018, 1, 1)


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
        not_full_year = (self.birth_date.month, self.birth_date.day) > (CURRENT_DATE.month, CURRENT_DATE.day)
        return (CURRENT_DATE.year - self.birth_date.year) - not_full_year

    def work(self):
        prefix = self.PREFIX[self.gender]
        return f"{prefix} a {self.job}"

    def money(self):
        return f"{self.salary * self.working_years * 12:_}".replace("_", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"
