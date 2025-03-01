from datetime import date


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
        split_date = self.birth_date.split(".")
        birth_date = date(int(split_date[2]), int(split_date[1]), int(split_date[0]))
        today = date.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def work(self):
        if self.gender == "male":
            return f"He is a {self.job}"
        elif self.gender == "female":
            return f"She is a {self.job}"
        else:
            return f"Is a {self.job}"

    def money(self):
        return f"{self.working_years * self.salary * 12:_}".replace("_", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"


if __name__ == '__main__':
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 42, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
