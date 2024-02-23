from datetime import date

Today = date(2018, 1, 1)


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
        # today = date(2018, 1, 1)
        birth_date = date(int(self.birth_date.split('.')[2]), int(self.birth_date.split('.')[1]),
                          int(self.birth_date.split('.')[0]))
        age = Today.year - birth_date.year - ((Today.month, Today.day) < (birth_date.month, birth_date.day))
        return age

    def work(self):
        if self.gender is "male":
            return f"He is a {self.job}"
        elif self.gender is "female":
            return f"She is a {self.job}"
        else:
            return f"Is a {self.job}"

    def money(self):
        money = (self.working_years * 12) * self.salary
        return f"{money:,}".replace(',', ' ')

    def home(self):
        return f"Lives in {self.city}, {self.country}"
