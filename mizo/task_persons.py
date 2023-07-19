from datetime import datetime


class Person:
    def __init__(self, first_name, last_name, date_of_birth, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

        # Additional attributes
        self.full_name = self.name()
        self.age_person1 = self.age()
        self.age_person2 = self.age()
        self.home_location_person1 = self.home()
        self.home_location_person2 = self.home()
        self.money_formatted = "{:,}".format(self.money())

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def work_person1(self):
        return self.job

    def money(self):
        return self.salary * self.working_years

    def home(self):
        return self.city, self.country

    def age(self):
        today = datetime(2018, 1, 1)
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


# Create instances of the Person class
person1_date_of_birth = datetime(1979, 9, 19)
person2_date_of_birth = datetime(1995, 12, 5)
person1 = Person('John', 'Smith', person1_date_of_birth, 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
person2 = Person('Hanna Rose', 'May', person2_date_of_birth, 'designer', 2.2, 2150, 'Austria', 'Vienna', 'unknown')

# Access additional attributes
print(
    f"Person('{person1.first_name}', '{person1.date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, '{person1.country}', '{person1.city}', '{person1.gender}') == {person1.full_name}")
print(
    f"Person('{person1.first_name}', '{person1.date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, '{person1.country}', '{person1.city}', '{person1.gender}') == {person1.age_person1}")
print(
    f"Person('{person1.first_name}', '{person1.date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, '{person1.country}', '{person1.city}', '{person1.gender}') == is a {person1.job}")
print(
    f"Person('{person1.first_name}', '{person1.date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, '{person1.country}', '{person1.city}', '{person1.gender}') == {person1.money_formatted}")
print(
    f"Person('{person1.first_name}', '{person1.date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, '{person1.country}', '{person1.city}', '{person1.gender}') == lives in {person1.home_location_person1}")

print(
    f"Person('{person2.first_name}', '{person2.date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, '{person2.country}', '{person2.city}' == {person2.full_name}")
print(
    f"Person('{person2.first_name}', '{person2.date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, '{person2.country}', '{person2.city}' == {person2.age_person2}")
print(
    f"Person('{person2.first_name}', '{person2.date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, '{person2.country}', '{person2.city}' == is a {person2.job}")
print(
    f"Person('{person2.first_name}', '{person2.date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, '{person2.country}', '{person2.city}' == {person2.money_formatted}")
print(
    f"Person('{person2.first_name}', '{person2.date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, '{person2.country}', '{person2.city}' == lives in {person2.home_location_person2}")
