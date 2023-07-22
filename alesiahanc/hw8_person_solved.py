from datetime import datetime


class Person:
    def __init__(
            self,
            first_name,
            last_name,
            birth_date,
            job,
            working_years,
            salary,
            country,
            city,
            gender="unknown",
    ):
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
        return self.first_name + " " + self.last_name

    def age(self):
        today = datetime.strptime("01.01.2018", "%d.%m.%Y")
        birth_date = datetime.strptime(self.birth_date, "%d.%m.%Y")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def work(self):
        if self.gender == "female":
            pronounce = "She is a "
        elif self.gender == "male":
            pronounce = "He is a "
        else:
            pronounce = "Is a "
        return f"{pronounce}{self.job}"

    def money(self):
        wealth = self.working_years * 12 * self.salary
        converted_wealth = f"{wealth:,}".replace(",", " ")
        return converted_wealth

    def home(self):
        return f"Lives in {self.city}, {self.country}"


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person(
        "John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male"
    )
    p2 = Person(
        "Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna"
    )

    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
