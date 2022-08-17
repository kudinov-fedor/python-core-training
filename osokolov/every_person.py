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
        self.current_date = '01.01.2018'
        self.days_in_year = 365.2425

    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def age(self) -> int:
        current = datetime.strptime(self.current_date, '%d.%m.%Y')
        birth = datetime.strptime(self.birth_date, '%d.%m.%Y')
        return int((current - birth).days // self.days_in_year)

    def work(self) -> str:
        pronouns = None
        match self.gender:
            case 'male':
                pronouns = 'He'
            case 'female':
                pronouns = 'She'
            case 'unknown':
                pronouns = 'Is'
        return f'{pronouns} a {self.job}'

    def money(self) -> str:
        amount_money = 12 * self.working_years * self.salary
        return format(amount_money, ',').replace(',', ' ')

    def home(self):
        return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", 'Name'
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
