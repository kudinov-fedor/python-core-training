# Details:  https://py.checkio.org/mission/every-person-is-unique/share/1c6fd4b663f7e40fa15b699f17efab40/
from datetime import datetime


CURRENT_DATE = datetime.strptime("01.01.2018", "%d.%m.%Y")


class Person:

    WORK_PREFIX = {
        "male": "He is a",
        "female": "She is a",
        "unknown": "Is a"
    }

    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city,
                 gender="unknown"):
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
        # Decrease by 1 if year is not full(bool converts to 0 or 1)
        year_not_full = (CURRENT_DATE.month, CURRENT_DATE.day) < (self.birth_date.month, self.birth_date.day)
        age = CURRENT_DATE.year - self.birth_date.year - year_not_full
        return age

    def work(self):
        return f"{self.WORK_PREFIX[self.gender]} {self.job}"

    def money(self):
        calculated_salary = self.working_years * self.salary * 12
        return '{:,}'.format(calculated_salary).replace(',', ' ')

    def home(self):
        return f"Lives in {self.city}, {self.country}"
