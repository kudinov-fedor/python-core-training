from datetime import date, datetime


TODAY = date(2018, 1, 1)


class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
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
        birth_date = datetime.strptime(self.birth_date, '%d.%m.%Y').date()
        age = TODAY.year - birth_date.year - ((TODAY.month, TODAY.day) < (birth_date.month, birth_date.day))
        return age

    def work(self):
        prefix = "Is"
        if self.gender is "male":
            prefix = "He is"
        elif self.gender is "female":
            prefix = "She is"
        return f"{prefix} a {self.job}"

    def money(self):
        money = (self.working_years * 12) * self.salary
        return f"{money:,}".replace(',', ' ')

    def home(self):
        return f"Lives in {self.city}, {self.country}"
