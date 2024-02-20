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
        today = date(2018, 1, 1)
        birth_date = date(int(self.birth_date.split('.')[2]), int(self.birth_date.split('.')[1]), int(self.birth_date.split('.')[0]))
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def work(self):
        return f"Is a {self.job}"

    def money(self):
        money = (self.working_years * 12) * self.salary
        return f"{money:,}".replace(',', ' ')

    def home(self):
        return f"Lives in {self.city}, {self.country}"


# if __name__ == '__main__':
#     p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
#     p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
#     assert p1.name() == "John Smith", "Name"
#     assert p1.age() == 38, "Age"
#     assert p2.work() == "Is a designer", "Job"
#     assert p1.money() == "648 000", "Money"
#     assert p2.home() == "Lives in Vienna, Austria", "Home"
