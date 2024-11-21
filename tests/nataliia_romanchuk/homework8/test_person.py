from nataliia_romanchuk.homework_8.every_person import Person


def test_new_person1():
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    assert p1.name() == "John Smith", "Person's Name"
    assert p1.age() == 44, "Person's Age"
    assert p1.work() == "He is a welder", "Person's Job"
    assert p1.money() == "648 000", "Person's Money"
    assert p1.home() == "Lives in Vancouver, Canada", "Person's Home"


def test_new_person2():
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna", "female")
    assert p2.name() == "Hanna Rose May", "Person's Name"
    assert p2.age() == 28, "Person's Age"
    assert p2.work() == "She is a designer", "Person's Job"
    assert p2.money() == "56 760", "Person's Money"
    assert p2.home() == "Lives in Vienna, Austria", "Person's Home"


def test_new_person3():
    p3 = Person("Rose", "Mary", "01.01.2024", "baby", 0, 0, "Austria", "Vienna")
    assert p3.name() == "Rose Mary", "Person's Name"
    assert p3.age() == 0, "Person's Age"
    assert p3.work() == "Is a baby", "Person's Job"
    assert p3.money() == "0", "Person's Money"
    assert p3.home() == "Lives in Vienna, Austria", "Person's Home"
