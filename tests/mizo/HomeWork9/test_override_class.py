from mizo.task_override_person_class import Person

person1 = Person("Alice", 30, "Engineer")
person2 = Person("Bob", 25, "Teacher")
person3 = Person("Charlie", 40, "Doctor")
person4 = "Bob"


def check_person_in_list():
    assert person1 in Person.get_instances()
    assert person2 in Person.get_instances()
    assert person3 in Person.get_instances()
    assert person4 not in Person.get_instances()


def test_my_persons():
    assert person1.name == "Alice"
    assert person2.age == 25
    assert person3.occupation != "Teacher"


def test_my_string():
    expected_str = "Name: Alice, Age: 30, Occupation: Engineer"
    assert str(person1) == expected_str
