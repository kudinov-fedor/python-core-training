import yspryn.hw8.every_person
from yspryn.hw8.every_person import Person
import pytest
from datetime import date


def test_every_person():
    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    p3 = Person("Lindsey", "Vonn", "19.09.1979", "ski racer", 15, 3600, "Canada", "Vancouver", "female")

    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p1.work() == "He is a welder", "Job"
    assert p2.work() == "Is a designer", "Job"
    assert p3.work() == "She is a ski racer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"


@pytest.mark.parametrize("birth, res", [("02.02.1988", 30),
                                        ("03.02.1988", 29),
                                        ("31.12.1987", 30),
                                        ("01.02.1988", 30),
                                        ("02.03.1988", 29),
                                        ("02.01.1988", 30)])
def test_my_function_with_mock(monkeypatch, birth, res):
    substitute_today = date(2018, 2, 2)
    monkeypatch.setattr("yspryn.hw8.every_person.TODAY", substitute_today)
    p0 = Person("John", "Smith", birth, "welder", 15, 3600, "Canada", "Vancouver", "male")
    assert p0.age() == res, "Age"
