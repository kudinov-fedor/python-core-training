"""https://py.checkio.org/en/mission/every-person-is-unique"""
from datetime import datetime


class Person:
    def __init__(self, first_name: str, last_name: str, birth_date: str, job: str, working_years: int, salary: int,
                 country: str, city: str, gender='unknown'):
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
        current_date = datetime(2018, 1, 1)
        partial_year = (self.birth_date.month, self.birth_date.day) > (current_date.month, current_date.day)
        return current_date.year - self.birth_date.year - partial_year

    def work(self):
        appeal = "is a"
        if self.gender == "male":
            appeal = f"He {appeal}"
        elif self.gender == "female":
            appeal = f"She {appeal}"
        return f"{appeal.capitalize()} {self.job}"

    def money(self):
        return f"{self.working_years * 12 * self.salary:_}".replace("_", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"


if __name__ == '__main__':
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
