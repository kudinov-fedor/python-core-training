from datetime import datetime


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
        current_date = datetime.strptime("01.01.2018", "%d.%m.%Y")
        birthdate = datetime.strptime(self.birth_date, "%d.%m.%Y")
        difference = current_date - birthdate
        full_years = difference.days // 365
        return full_years

    def work(self):
        if self.gender == "male":
            return f"He is a {self.job}"
        if self.gender == "female":
            return f"She is a {self.job}"
        else:
            return f"Is a {self.job}"

    def money(self):
        total_amount = str(self.working_years * 12 * self.salary)
        count = 0
        tem_list = []
        result = ""
        for i in str(total_amount):
            count += 1
            tem_list.append(i)
            if count % 3 == 0:
                tem_list.append(" ")
        for el in tem_list:
            result += el
        return result.rstrip(" ")

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
