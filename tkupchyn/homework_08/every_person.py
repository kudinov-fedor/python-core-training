# Details:  https://py.checkio.org/mission/every-person-is-unique/share/1c6fd4b663f7e40fa15b699f17efab40/
from datetime import datetime, date


class Person:
    pronoun = {'male': 'He is a',
               'female': 'She is a',
               'unknown': 'Is a'}

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

    # @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    # @property
    def age(self):
        today = datetime.now()
        birth_date = datetime.strptime(self.birth_date, '%d.%m.%Y').date()
        years = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            years -= 1

        return years

    def work(self):
        return f'{self.__class__.pronoun[self.gender]} {self.job}'

    def money(self):
        return '{:,}'.format(self.salary * self.working_years * 12).replace(',', ' ')

    def home(self):
        return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    print(p1.age())
    print(p1.work())
    print(p2.work())
    print(p1.money())
    assert p1.age() == 45, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"