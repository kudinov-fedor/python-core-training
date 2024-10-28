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

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self) -> int:
        today = datetime.now()
        birth_date = datetime.strptime(self.birth_date, '%d.%m.%Y').date()
        years = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            years -= 1

        return years

    @property
    def work(self) -> str:
        return f'{self.__class__.pronoun[self.gender]} {self.job}'

    @property
    def money(self) -> str:
        return '{:,}'.format(int(self.salary * self.working_years * 12)).replace(',', ' ')

    @property
    def home(self) -> str:
        return f'Lives in {self.city}, {self.country}'
