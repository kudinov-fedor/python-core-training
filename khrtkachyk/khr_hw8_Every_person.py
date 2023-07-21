from datetime import datetime, date
import locale

TODAY = date(2023, 7, 21)


class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        """
        Returns the full name (name and surname, separated by a whitespace).
        """
        return f'{self.first_name} {self.last_name}'

    def age(self):
        """
        Returns the person’s age - the number of fully lived years, based on current date.
        """
        age = TODAY.year - self.birth_date.year - ((TODAY.month, TODAY.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def work(self):
        """
        Returns the person’s job in a sentence as follows: ‘He is a ...’ (if male) ‘She is a ...’ (if female)
        ‘Is a ...’ (if unknown)
        """
        if self.gender == "male":
            return f'He is a {self.job}'
        elif self.gender == "female":
            return f'She is a {self.job}'
        else:
            return f'Is a {self.job}'

    def money(self):
        """
        Returns an amount of money, earned during the working years. Returned in format 'xx xxx'.
        """
        return "{:,}".format(self.salary * self.working_years * 12).replace(",", " ")

    def home(self):
        """
        Returns the country and the city where a person lives: ‘Lives in the city, country’.
        """
        return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith"
    assert p1.age() == 43
    assert p2.work() == "Is a designer"
    assert p1.money() == "648 000"
    assert p2.home() == "Lives in Vienna, Austria"
