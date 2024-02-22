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


def test_person():
    assert p.name() == "John Smith", "Name"
    assert p.age() == 44, "Age"
    assert p.work() == "Is a welder", "Job"
    assert p.money() == "648 000", "Money"
    assert p.home() == "Lives in Vancouver, Canada", "Home"
