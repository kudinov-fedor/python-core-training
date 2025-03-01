from irepela.homework_8.every_person import Person


def test_first_person():
    p1 = Person("John", "Smith", "19.09.1979", "welder",
                15, 3600, "Canada", "Vancouver", "male")
    assert p1.name() == "John Smith"
    assert p1.age() == 38
    assert p1.money() == "648 000"


def test_second_person():
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer",
                2.2, 2150, "Austria", "Vienna")
    assert p2.work() == "Is a designer"
    assert p2.home() == "Lives in Vienna, Austria"
