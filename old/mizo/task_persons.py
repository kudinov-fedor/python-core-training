from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, date_of_birth, job, working_years, salary, country, city,
                 gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return self.first_name + " " + self.last_name

    def work(self):
        return self.job

    def money(self):
        return self.salary * self.working_years

    def home(self):
        return f"{self.city}, {self.country}"

    def age(self):
        today = datetime(2018, 1, 1)
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
