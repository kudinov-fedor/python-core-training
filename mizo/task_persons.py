import datetime


class Person:
    def __init__(self, first_name, last_name, date_of_birth, job, working_years, salary, country, city, gender):
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
        return f"{self.first_name} {self.last_name}"  # concatenation

    def age(self):
        today = datetime.datetime(2018, 1, 1)
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

    def work_person1(self):
        return self.job

    def money(self):
        return self.salary * self.working_years

    def home(self):
        return self.city, self.country


person1_date_of_birth = datetime.datetime(1979, 9, 19)
person2_date_of_birth = datetime.datetime(1995, 12, 5)
# Create an instance of the Person class
person1 = Person('John', 'Smith', person1_date_of_birth, 'welder', 15, 3600, 'Canada', 'Vancouver', 'male')
person2 = Person('Hanna Rose', 'May', person2_date_of_birth, 'designer', 2.2, 2150, 'Austria', 'Vienna', 'unknown')

# Call the name() method to get the full name
person1.full_name = person1.name()
person2.full_name = person2.name()
age = person1.age()
age_person2 = person2.age()
money_formatted = "{:,}".format(person1.money())
money_formatted_person2 = "{:,}".format(person2.money())
home_person1 = person1.home()
home_person2 = person2.home()

print(
    f"Person( '{person1.first_name}', '{person1_date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, {person1.country}, {person1.city}, {person1.gender}) == {person1.full_name}")
print(
    f"Person( '{person1.first_name}', '{person1_date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, {person1.country}, {person1.city}, {person1.gender}) == {age}")
print(
    f"Person( '{person1.first_name}', '{person1_date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, {person1.country}, {person1.city}, {person1.gender}) == is a {person1.job}")
print(
    f"Person( '{person1.first_name}', '{person1_date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, {person1.country}, {person1.city}, {person1.gender}) == {money_formatted}")
print(
    f"Person( '{person1.first_name}', '{person1_date_of_birth}', '{person1.job}', {person1.working_years}, {person1.salary}, {person1.country}, {person1.city}, {person1.gender}) == lives in {home_person1}")

print(
    f"Person( '{person2.first_name}', '{person2_date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, {person2.country}, {person2.city}, {person2.gender}) == {person2.full_name}")
print(
    f"Person( '{person2.first_name}', '{person2_date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, {person2.country}, {person2.city}, {person2.gender}) == {age_person2}")
print(
    f"Person( '{person2.first_name}', '{person2_date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, {person2.country}, {person2.city}, {person2.gender}) == is a {person2.job}")
print(
    f"Person( '{person2.first_name}', '{person2_date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, {person2.country}, {person2.city}, {person2.gender}) == {money_formatted_person2}")
print(
    f"Person( '{person2.first_name}', '{person2_date_of_birth}', '{person2.job}', {person2.working_years}, {person2.salary}, {person2.country}, {person2.city}, {person2.gender}) == lives in{home_person2}")
