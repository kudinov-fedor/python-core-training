from mizo.task_persons import Person
from datetime import datetime

person1_date_of_birth = datetime(1979, 9, 19)
person2_date_of_birth = datetime(1995, 12, 5)

p1 = Person("John", "Smith", person1_date_of_birth, "welder", 15, 3600, "Canada", "Vancouver", "male")
p2 = Person("Hanna Rose", "May", person2_date_of_birth, "designer", 2.2, 2150, "Austria", "Vienna")


def test_attr_person1():
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p1.work() == "welder", "Job"
    assert p1.money() == 54000, "Money"
    assert p1.home() == "Vancouver, Canada", "Home"


def test_attr_person2():
    assert p2.name() == "Hanna Rose May", "Name"
    assert p2.age() == 22, "Age"
    assert p2.work() == "designer", "Job"
    assert p2.money() == 4730, "Money"
    assert p2.home() == "Vienna, Austria", "Home"
