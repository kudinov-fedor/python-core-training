import hw8_persons


p1 = hw8_persons.Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
p2 = hw8_persons.Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")


def test_person1():
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p1.money() == "648 000", "Money"
    assert p1.home() == "Lives in Vancouver, Canada", "Home"
    assert p1.work() == "Is a welder", "Job"


def test_person2_full_name():
    full_name = p2.name()
    assert full_name == "Hanna Rose May", "Name"


def test_person2_age():
    person_age = p2.age()
    assert person_age == 22, "Age"


def test_person2_home():
    person_home = p2.home()
    assert person_home == "Lives in Vienna, Austria", "Home"


def test_person2_money():
    total_rewards = p2.money()
    assert total_rewards == "56 760.0", "Money"


def test_person2_work():
    person_work = p2.work()
    assert person_work == "Is a designer", "Job"
