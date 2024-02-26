from anmykh.homework.homework_8_persons import Person

p = Person("John",
           "Smith",
           "19.09.1979",
           "welder",
           15,
           3600,
           "Canada",
           "Vancouver",
           "male")


p2 = Person("Ana",
            "Sad",
            "28.01.2000",
            "designer",
            6,
            1200,
            "Ukraine",
            "Kyiv",
            "female")


def test_person():
    assert p.name() == "John Smith", "Name"
    assert p.age() == 44, "Age"
    assert p.work() == "He is a welder", "Job"
    assert p.money() == "648 000", "Money"
    assert p.home() == "Lives in Vancouver, Canada", "Home"


def test_person2():
    assert p2.name() == "Ana Sad", "Name"
    assert p2.age() == 24, "Age"
    assert p2.work() == "She is a designer", "Job"
    assert p2.money() == "86 400", "Money"
    assert p2.home() == "Lives in Kyiv, Ukraine", "Home"
