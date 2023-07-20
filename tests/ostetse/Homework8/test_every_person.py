from datetime import datetime

CURRENT_DATE = datetime(2017, 1, 1)


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
        return CURRENT_DATE.year - self.birth_date.year

    def work(self):
        prefix = self.PREFIX[self.gender]
        return f"{prefix} a {self.job}"

    def money(self):
        return f"{self.salary * self.working_years * 12:_}".replace("_", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"


def test_person():
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
